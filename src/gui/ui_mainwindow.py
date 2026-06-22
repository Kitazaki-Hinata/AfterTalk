import os
import logging
from typing import Optional, Any

from . import *
from .ui_main import Ui_MainWindow
from .ui_function import Ui_Function

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # type: ignore
        self.ui_functions = Ui_Function(self)

        # 录音部分 功能对接


        # 底稿转录部分 功能对接
        self.btn_select_vocal.clicked.connect(
            lambda: self.ui_functions.select_file("音频文件 (*.wav *.mp3)", self.vocal_file_path)
        )
        self.btn_select_model.clicked.connect(
            lambda: self.ui_functions.select_file("所有文件 (*.*)", self.model_file_path)
        )

        # 会议纪要部分 功能对接