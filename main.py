'''
启动GUI界面。对接后端功能的部分在gui/ui_function.py中实现。
'''

import sys
from PySide6.QtWidgets import QApplication
from src.gui.ui_mainwindow import MainWindow
from src.config.paths import ensure_output_dirs
from src.utils.logger import get_logger


def main():
    ensure_output_dirs()  # 确保子目录存在
    log = get_logger(__name__)
    log.info("AfterTalk 启动")

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
