'''启动GUI界面。对接后端功能的部分在gui/ui_function.py中实现。'''

import sys
from PySide6.QtWidgets import QApplication
from src.gui.ui_mainwindow import MainWindow


def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
