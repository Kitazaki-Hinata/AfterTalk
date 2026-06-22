import os
from . import *
import logging
from typing import Optional, Any


class Ui_Function:
    def __init__(self, main_window):
        self.main_window = main_window

    # 选择文件function, 传入参数：文件类型，路径输出部件
    def select_file(self, file_type: str = "*.*", line_edit: Optional[QLineEdit] = None):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.main_window, "选择文件", "", file_type)
        
        if file_path:
            if line_edit:
                line_edit.setText(file_path)
            else:
                logging.warning("未提供line_edit参数，无法显示选择的文件路径。")
