'''
gui槽函数文件，集中所有函数
对接gui界面与后端功能
'''


import os
import time
import inspect
from . import *
from typing import Optional, Any, Callable
from src.utils.logger import get_logger

log = get_logger(__name__)


class _Worker(QObject):
    '''
    通用后台线程 Worker：在子线程中执行任意阻塞函数 func(*args, **kwargs)，
    通过信号把进度和结果传回主线程，避免 GUI 卡顿。
    '''
    progress = Signal(str)      # 转发给 console_output（在主线程安全更新 QTextEdit）
    finished = Signal(object)   # 返回结果：func 的返回值，出错时为 None

    def __init__(self, func: Callable, args: tuple, kwargs: dict):
        super().__init__()
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def run(self):
        try:
            result = self._func(*self._args, **self._kwargs)
        except Exception as e:
            name = getattr(self._func, "__name__", str(self._func))
            log.error(f"后台线程执行 {name} 异常：{e}")
            self.progress.emit(f"任务执行出错：{e}")
            result = None
        self.finished.emit(result)


class Ui_Function:
    def __init__(self, main_window):
        self.main_window = main_window
        self._threads: set = set()  # 持有运行中的(线程, worker)，防止被GC回收

    # 控制台输入输出
    def console_output(self, message: str):
        self.main_window.console_text.append(f"{time.strftime('%H:%M:%S')}:  {message}")  # QTextEdit控件添加内容

    # 选择文件function, 传入参数：文件类型，路径输出部件
    def select_file(self, file_type: str = "*.*", line_edit: Optional[QLineEdit] = None):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.main_window, "选择文件", "", file_type)
        
        if file_path:
            if line_edit:
                line_edit.setText(file_path)
            else:
                log.error("未提供line_edit参数，无法显示选择的文件路径。")

    # 打开文件夹
    def open_folder(self, folder_path: str):
        if os.path.isdir(folder_path):
            os.startfile(folder_path)
        else:
            log.error(f"提供的路径不是有效的文件夹: {folder_path}")

    # 打开文件
    def open_file(self, file_path: str, console_text : str = "正在打开文件。"):
        self.console_output(console_text)
        if os.path.isfile(file_path):
            os.startfile(file_path)
        else:
            log.error(f"提供的路径不是有效的文件: {file_path}")

    # 打开浏览器
    def open_browser(self, url: str):
        import webbrowser
        webbrowser.open(url)

    # 处理.env输入
    def handle_env_input(self, line_edit: QLineEdit):
        api = line_edit.text().strip()
        if api and api.startswith("sk-"):
            from src.config.paths import ENV_FILE
            ENV_FILE.write_text(f"API_KEY={api}\n", encoding="utf-8")
            self.console_output("API Key 已保存到 .env 文件。")
        elif not api.startswith("sk-"):
            log.error("API Key 格式不正确，应以 'sk-' 开头。")
            self.console_output("API Key 格式不正确，应以 'sk-' 开头。")



    '''对接后端的功能函数'''
    # 生成会议纪要，调用llm
    def generate_minutes(self, model : str, skill_checkbox : Any):
        self.console_output(f"开始生成会议纪要，使用模型: {model}")
        from src.llm.llm_client import create_client, ds_requests

        # 获取输入的底稿文件路径
        try:
            txt_file_path : str = self.main_window.txt_file_path.text().strip()
            if txt_file_path:
                self.console_output(f"正在处理文件: {txt_file_path}")
            else:
                log.warning("未找到txt文本，请检查传入的文件是否正确")
                self.console_output("未找到txt文本，请检查传入的文件是否正确")
                return
        except:
            log.warning("未找到txt文本，请检查传入的文件是否正确")
            self.console_output("未找到txt文本，请检查传入的文件是否正确")
            return

        # 首先读取API KEY
        from dotenv import load_dotenv
        from src.config.paths import ENV_FILE   
        load_dotenv(ENV_FILE, override=True)
        api_key = os.getenv("API_KEY")
        if not api_key:
            log.error("未找到 API_KEY，请在 .env 文件中配置。")
            self.console_output("未找到 API_KEY，请在 .env 文件中配置。")
            return
        if not api_key.startswith("sk-"):
            log.error("API Key 格式不正确，应以 'sk-' 开头。")
            self.console_output("API Key 格式不正确，应以 'sk-' 开头。")
            return

        ''' 将api key传入到llm_client，生成client然后发送信息
        response txt是从ds返回回来的会议纪要'''
        # 创建client
        client = create_client(api_key)

        # 检查checkbox是否需要调用skill.md
        skill = "skill" if skill_checkbox.isChecked() else None

        # 将阻塞的网络请求放到后台线程执行，防止GUI卡顿
        # ds_requests 含 console_output 参数，run_async 会自动注入信号发射器
        self.run_async(
            ds_requests,
            txt_file_path,
            skill_name=skill,
            model=model,
            client=client,
            on_finished=self._on_minutes_finished,
            disable_widget=self.main_window.btn_minutes,
        )

    # 会议纪要生成完成（成功或失败）的回调，运行在主线程
    def _on_minutes_finished(self, result: Optional[str]):
        if result:
            self.console_output("会议纪要生成完成。请查看output/minutes目录")
            print(result)
        # 失败时 ds_requests 已通过 console_output 给出中文提示，无需重复


    # 调用本地whisper模型生成transcript
    def generate_transcript(self, model_file_path : str, audio_file_path : str):
        from src.whisper.whisper import whisper_generate_transcript

        # 校验模型与音频文件路径是否已填写
        if not model_file_path:
            log.warning("未选择 whisper 模型文件")
            self.console_output("请先选择 whisper 模型文件。")
            return
        if not audio_file_path:
            log.warning("未选择音频文件")
            self.console_output("请先选择需要转录的音频文件。")
            return

        self.console_output(f"开始生成会议文本转录，使用模型: {model_file_path}")

        # whisper 转录是重度阻塞操作，放到后台线程执行，防止GUI卡顿
        # whisper_generate_transcript 含 console_output 参数，run_async 会自动注入信号发射器
        self.run_async(
            whisper_generate_transcript,
            model_file_path,
            audio_file_path,
            on_finished=self._on_transcript_finished,
            disable_widget=self.main_window.btn_start_trans,
        )

    # 转录完成（成功或失败）的回调，运行在主线程
    def _on_transcript_finished(self, result: Optional[str]):
        if result:
            self.console_output("会议文本转录完成。请查看output/transcript目录")
        # 失败时 whisper_generate_transcript 已通过 console_output 给出中文提示，无需重复



    '''通用后台线程执行器'''
    # 在子线程运行 func(*args, **kwargs)，避免阻塞GUI。
    # 若 func 接受 console_output 参数则自动注入，使其输出经信号回到主线程。
    #   on_finished:   任务结束回调(主线程)，参数为 func 返回值
    #   disable_widget: 运行期间禁用、结束后恢复的控件（如按钮，防重复点击）
    def run_async(
        self,
        func: Callable,
        *args,
        on_finished: Optional[Callable[[Any], None]] = None,
        disable_widget: Any = None,
        **kwargs,
    ) -> QThread:
        thread = QThread()
        worker = _Worker(func, args, kwargs)

        # 若目标函数支持 console_output，注入信号发射器（跨线程安全更新GUI）
        if "console_output" not in kwargs and self._accepts_console_output(func):
            worker._kwargs["console_output"] = worker.progress.emit

        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.progress.connect(self.console_output)

        def _done(result):
            if disable_widget is not None:
                disable_widget.setEnabled(True)
            if on_finished is not None:
                on_finished(result)

        worker.finished.connect(_done)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)

        # 持有引用防止被GC，线程结束后移除
        handle = (thread, worker)
        self._threads.add(handle)
        thread.finished.connect(lambda: self._threads.discard(handle))

        if disable_widget is not None:
            disable_widget.setEnabled(False)
        thread.start()
        return thread

    # 判断函数是否接受 console_output 参数
    @staticmethod
    def _accepts_console_output(func: Callable) -> bool:
        try:
            return "console_output" in inspect.signature(func).parameters
        except (TypeError, ValueError):
            return False


