'''
主界面控件与信号对接
'''

import os
import logging
from typing import Optional, Any

from . import *
from .ui_main import Ui_MainWindow
from .ui_function import Ui_Function
from src.config.paths import RECORDINGS_DIR, TRANSCRIPT_DIR, MINUTES_DIR, MODEL_DIR, SKILL_DIR, ENV_FILE

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.ui_functions = Ui_Function(self)

        # 打开GUI后默认加载的内容
        # 读取.env文件的内容，加载到line edit当中

        if ENV_FILE.exists():
            env_content = ENV_FILE.read_text(encoding="utf-8")
            for line in env_content.splitlines():
                if line.startswith("API_KEY="):
                    api_key : str = line.split("=", 1)[1].strip()
                    self.api_entry.setText(api_key)
                    break
        
        # 下拉框中展示所有ds model
        from src.llm.llm_client import AVAILABLE_MODELS
        self.ds_model_combobox.addItems(AVAILABLE_MODELS)


        '''录音部分 功能对接'''
        # 打开文件夹
        self.btn_record_folder.clicked.connect(
            lambda: self.ui_functions.open_folder(str(RECORDINGS_DIR))
        )

        # 开始录音：传入命名框文件名（不含后缀，留空则默认日期时间）
        self.btn_start_record.clicked.connect(
            lambda: self.ui_functions.start_recording(self.rename_file_box.text())
        )

        # 停止录音并自动转录
        self.btn_end_record.clicked.connect(
            lambda: self.ui_functions.stop_recording()
        )
        # 未开始录音时停止按钮不可用
        self.btn_end_record.setEnabled(False)


        '''底稿转录部分 功能对接'''
        # 选择文件并获得路径
        self.btn_select_vocal.clicked.connect(
            lambda: self.ui_functions.select_file("音频文件 (*.wav *.mp3)", self.vocal_file_path)
        )
        self.btn_select_model.clicked.connect(
            lambda: self.ui_functions.select_file("模型文件 (*.bin)", self.model_file_path)
        )

        # 打开文件夹
        self.btn_trans_folder.clicked.connect(
            lambda: self.ui_functions.open_folder(str(TRANSCRIPT_DIR))
        )
        self.btn_model_folder.clicked.connect(
            lambda: self.ui_functions.open_folder(str(MODEL_DIR))
        )

        # 运行本地模型并转录
        self.btn_start_trans.clicked.connect(
            lambda: self.ui_functions.generate_transcript(self.model_file_path.text(), self.vocal_file_path.text())
        )

        # 一键生成文档
        self.btn_trans_and_minutes.clicked.connect(
            lambda: self.ui_functions.one_time_transcript_and_minutes(
                self.model_file_path.text(),
                self.vocal_file_path.text(),
                self.ds_model_combobox.currentText(),
                self.skill_checkbox
            )
        )

        '''会议纪要部分 功能对接'''
        # 选择文件并获得路径
        self.btn_select_txt.clicked.connect(
            lambda: self.ui_functions.select_file("文本文件 (*.txt)", self.txt_file_path)
        )

        # 打开文件夹，文件或浏览器
        self.btn_open_skill.clicked.connect(
            lambda: self.ui_functions.open_file(str(SKILL_DIR / "skill.md"), console_text = "编辑skill.md的时候需要参照前面的格式。不要删除特殊字符，比如'#', '|' 等，可以修改语句和语句内的标点符号。")
        )
        self.btn_minute_folder.clicked.connect(
            lambda: self.ui_functions.open_folder(str(MINUTES_DIR))
        )
        self.btn_ds_open_web.clicked.connect(
            lambda: self.ui_functions.open_browser("https://platform.deepseek.com/sign_in")
        )

        # API KEY 传入
        self.btn_api.clicked.connect(
            lambda:self.ui_functions.handle_env_input(self.api_entry)
        )

        # 生成会议纪要 对接DS API
        self.btn_minutes.clicked.connect(
            lambda: self.ui_functions.generate_minutes(self.ds_model_combobox.currentText(), self.skill_checkbox)
        )