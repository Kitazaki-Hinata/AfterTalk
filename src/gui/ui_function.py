'''
gui槽函数文件，集中所有函数
对接gui界面与后端功能
'''


import os
import time
from . import *
from typing import Optional, Any
from src.utils.logger import get_logger

log = get_logger(__name__)

class Ui_Function:
    def __init__(self, main_window):
        self.main_window = main_window

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
    def generate_minutes(self, model : Any, skill_checkbox : Any):
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

        response_txt = ds_requests(txt_file_path, skill_name=skill, model=model, client=client, console_output=self.console_output)
        print(response_txt)
        # if response_txt:
        #     self.console_output(response_txt)


