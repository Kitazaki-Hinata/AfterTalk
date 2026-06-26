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

        # 录音相关状态：录音器、计时器、已录秒数、本次录音锁定的文件名
        self._recorder = None                 # AudioRecorder，首次开始录音时惰性创建
        self._record_filename: str = ""       # 点击开始录音时锁定的文件名（不含后缀）
        self._record_elapsed: int = 0         # 已录制秒数，用于驱动 timer_show
        self._record_timer = QTimer()
        self._record_timer.setInterval(1000)  # 每秒触发一次，刷新计时显示
        self._record_timer.timeout.connect(self._tick_record_timer)

    # 控制台输入输出
    def console_output(self, message: str):
        self.main_window.console_text.append(f"{time.strftime('%H:%M:%S')}:  {message}")  # QTextEdit控件添加内容

    # 控制台强提示：红色加粗，用于重名/错误等需要最强提醒的场景
    def console_output_error(self, message: str):
        ts = time.strftime('%H:%M:%S')
        html = f'<span style="color:#ff0000; font-weight:bold;">⚠ {ts}:  {message}</span>'
        self.main_window.console_text.append(html)
        # 复位文本格式，避免后续普通日志继承红色加粗
        self.main_window.console_text.setTextColor(QColor("black"))
        self.main_window.console_text.setFontWeight(QFont.Weight.Normal)

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



    '''录音功能'''
    # 开始录音：锁定文件名、启动麦克风采集、计时归零并开始计时
    def start_recording(self, filename: str = ""):
        from src.audio.recorder import AudioRecorder

        if self._recorder is None:
            self._recorder = AudioRecorder()

        if self._recorder.is_recording:
            self.console_output("正在录音中，请先停止当前录音。")
            return

        # 重名检查：解析出实际文件名后，若 recordings 目录已有同名 wav，则中止本次录音并要求改名
        from src.config.paths import RECORDINGS_DIR
        resolved_name = AudioRecorder._resolve_filename(filename)
        if (RECORDINGS_DIR / f"{resolved_name}.wav").exists():
            self.console_output_error(
                f"文件名「{resolved_name}」已存在，本次录音已中止！请修改音频文件命名后重新开始录音。"
            )
            return

        # 在点击开始录音的此刻锁定文件名，避免录音过程中改动输入框影响结果
        self._record_filename = filename

        try:
            self._recorder.start(console_output=self.console_output)
        except Exception as e:
            log.error(f"启动录音失败：{e}")
            self.console_output(f"启动录音失败：{e}")
            return

        # 计时器归零后启动
        self._record_elapsed = 0
        self.main_window.timer_show.setTime(QTime(0, 0, 0))
        self._record_timer.start()

        # 按钮状态：录音期间禁用开始、启用停止，防止重复点击
        self.main_window.btn_start_record.setEnabled(False)
        self.main_window.btn_end_record.setEnabled(True)

    # 每秒刷新一次计时显示 timer_show
    def _tick_record_timer(self):
        self._record_elapsed += 1
        h, rem = divmod(self._record_elapsed, 3600)
        m, s = divmod(rem, 60)
        self.main_window.timer_show.setTime(QTime(h, m, s))

    # 停止录音：停表、停采集并落盘，随后自动转录该录音
    def stop_recording(self):
        if self._recorder is None or not self._recorder.is_recording:
            self.console_output("当前没有正在进行的录音。")
            return

        # 先停计时，再恢复按钮状态
        self._record_timer.stop()
        self.main_window.btn_start_record.setEnabled(True)
        self.main_window.btn_end_record.setEnabled(False)

        # 清除文件名称框
        self.main_window.rename_file_box.clear()

        try:
            audio_path = self._recorder.stop(self._record_filename, console_output=self.console_output)
        except Exception as e:
            log.error(f"停止录音失败：{e}")
            self.console_output(f"停止录音失败：{e}")
            return

        # 把录音路径填入音频文件框
        self.console_output(f"录音已保存：{audio_path}, 音频转录底稿部分已自动选择音频文件。")
        self.main_window.vocal_file_path.setText(audio_path)
        return


    '''对接后端的功能函数'''
    # 生成会议纪要，调用llm
    def generate_minutes(self, model : str, skill_checkbox : Any , extra_file_path : str|None = None):
        self.console_output(f"开始生成会议纪要，使用模型: {model}")
        from src.llm.llm_client import create_client, ds_requests

        # 获取输入的底稿文件路径
        try:
            if extra_file_path:
                txt_file_path : str = extra_file_path
            else:
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

        # 记录底稿文件名，生成的 Word 纪要将沿用同名，便于对应
        minutes_filename = os.path.splitext(os.path.basename(txt_file_path))[0]

        # 将阻塞的网络请求放到后台线程执行，防止GUI卡顿
        # ds_requests 含 console_output 参数，run_async 会自动注入信号发射器
        self.run_async(
            ds_requests,
            txt_file_path,
            skill_name=skill,
            model=model,
            client=client,
            on_finished=lambda result: self._on_minutes_finished(result, minutes_filename),
            disable_widget=self.main_window.btn_minutes,
        )

    # 会议纪要生成完成（成功或失败）的回调，运行在主线程
    def _on_minutes_finished(self, result: Optional[str], filename: Optional[str] = None):
        if result:
            # 将返回的会议纪要写入 output/minutes 下的 Word 文件
            from src.utils.word_writer import save_minutes_to_word
            save_minutes_to_word(result, filename=filename, console_output=self.console_output)
            self.console_output("会议纪要生成完成。请查看output/minutes目录")
        # 失败时 ds_requests 已通过 console_output 给出中文提示，无需重复


    # 调用本地whisper模型生成transcript
    def generate_transcript(self, model_file_path : str, audio_file_path : str) -> str | None:
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

    # 一键转录底稿+AI请求
    def one_time_transcript_and_minutes(
            self,
            model_file_path : str,
            audio_file_path : str,
            model : str,
            skill_checkbox : Any
    ):
        # 首先依次检查每个参数是否填入
        check_parameters = [
            (model_file_path, "whisper 模型文件"),
            (audio_file_path, "音频文件"),
            (model, "LLM 模型"),
        ]
        
        for value, message in check_parameters:
            if not value:
                self.console_output(f"{message}未填入。")
                log.warning(f"{message}未填入。")
                return

        from src.whisper.whisper import whisper_generate_transcript

        self.console_output(f"开始一键转录，使用模型: {model_file_path}")

        # whisper 在子线程执行，转录完成后才能拿到 txt 路径，
        # 把第二步（生成会议纪要）放到 on_finished 回调里，由信号触发
        # 用闭包捕获 model / skill_checkbox 供回调使用。
        def _on_transcript_done(txt_file_path: Optional[str]):
            if not txt_file_path:
                # 转录失败，whisper_generate_transcript 已通过 console_output 提示
                return
            self.console_output("转录完成，开始生成会议纪要...")
            # 将转录得到的路径作为底稿传给 generate_minutes
            self.generate_minutes(model, skill_checkbox, extra_file_path=txt_file_path)

        self.run_async(
            whisper_generate_transcript,
            model_file_path,
            audio_file_path,
            on_finished=_on_transcript_done,
            disable_widget=self.main_window.btn_trans_and_minutes,
        )



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


