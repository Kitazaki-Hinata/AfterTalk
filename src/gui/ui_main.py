# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 750)
        MainWindow.setMinimumSize(QSize(1150, 750))
        MainWindow.setStyleSheet(u"background: #ffeaeb;\n"
"border:0;\n"
"padding:0;\n"
"\n"
"/*\u5168\u5c40checkbox\u6837\u5f0f \u591a\u9009\u6846*/\n"
"QCheckBox {\n"
"            spacing: 8px;    /*\u591a\u9009\u6846\u4e0e\u5b57\u4f53\u7684\u7a7a\u683c*/\n"
"            font-size: 11px;\n"
"        }\n"
"        \n"
"QCheckBox::indicator {\n"
"            width: 12px;\n"
"            height: 12px;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            background: #202023;\n"
"        }\n"
"        \n"
"QCheckBox::indicator:hover {\n"
"            border: 1px solid #ffffff;\n"
"        }\n"
"\n"
"        \n"
"QCheckBox::indicator:checked {\n"
"            border: 1px solid #90b6e7;\n"
"            image: url(:/png/png/true.png);\n"
"        }\n"
"QCheckBox::indicator:disabled {\n"
"            border: 1px solid #454555;\n"
"            background: #454555;\n"
"        }\n"
"        \n"
"        QCheckBox::indicator:checked:disabled {\n"
"            background: #454555;\n"
"            border: 2px solid"
                        " #454555;\n"
"        }\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.label_widget = QWidget(self.centralwidget)
        self.label_widget.setObjectName(u"label_widget")
        self.label_widget.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_2 = QVBoxLayout(self.label_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, -1, -1, -1)
        self.topic_label = QLabel(self.label_widget)
        self.topic_label.setObjectName(u"topic_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.topic_label.setFont(font)

        self.verticalLayout_2.addWidget(self.topic_label)

        self.topic_two = QLabel(self.label_widget)
        self.topic_two.setObjectName(u"topic_two")

        self.verticalLayout_2.addWidget(self.topic_two)


        self.verticalLayout.addWidget(self.label_widget)

        self.settings_widget = QWidget(self.centralwidget)
        self.settings_widget.setObjectName(u"settings_widget")
        self.settings_widget.setMinimumSize(QSize(0, 300))
        self.settings_widget.setStyleSheet(u"background: #ffe0e1;\n"
"border-radius: 15px;")
        self.horizontalLayout = QHBoxLayout(self.settings_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.record_widget = QWidget(self.settings_widget)
        self.record_widget.setObjectName(u"record_widget")
        self.record_widget.setStyleSheet(u"background: #ffeaeb;\n"
"border-radius: 5px;")
        self.verticalLayout_4 = QVBoxLayout(self.record_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.record_label = QLabel(self.record_widget)
        self.record_label.setObjectName(u"record_label")
        self.record_label.setMinimumSize(QSize(0, 40))
        self.record_label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.record_label.setFont(font1)

        self.verticalLayout_4.addWidget(self.record_label)

        self.widget_2 = QWidget(self.record_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QPushButton {\n"
"	border-radius : 9px;\n"
"	minimum-height : 30px;\n"
"}\n"
"\n"
"/*download*/\n"
"QPushButton {\n"
"	background : #ffbfc0;\n"
"}\n"
"QPushButton::hover {\n"
"	background : #ffffff;\n"
"}\n"
"QPushButton::pressed {\n"
"	background : #ffbfc0;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.timer_widget = QWidget(self.widget_2)
        self.timer_widget.setObjectName(u"timer_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.timer_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.timer_label = QLabel(self.timer_widget)
        self.timer_label.setObjectName(u"timer_label")

        self.horizontalLayout_7.addWidget(self.timer_label)

        self.timer_show = QTimeEdit(self.timer_widget)
        self.timer_show.setObjectName(u"timer_show")
        self.timer_show.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_show.setReadOnly(True)
        self.timer_show.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.timer_show.setCurrentSection(QDateTimeEdit.Section.HourSection)

        self.horizontalLayout_7.addWidget(self.timer_show)


        self.verticalLayout_7.addWidget(self.timer_widget)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.rename_file_label = QLabel(self.widget_4)
        self.rename_file_label.setObjectName(u"rename_file_label")

        self.horizontalLayout_9.addWidget(self.rename_file_label)

        self.rename_file_box = QLineEdit(self.widget_4)
        self.rename_file_box.setObjectName(u"rename_file_box")
        self.rename_file_box.setStyleSheet(u"background:white")

        self.horizontalLayout_9.addWidget(self.rename_file_box)


        self.verticalLayout_7.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.btn_start_record = QPushButton(self.widget_5)
        self.btn_start_record.setObjectName(u"btn_start_record")
        self.btn_start_record.setMinimumSize(QSize(120, 20))

        self.horizontalLayout_8.addWidget(self.btn_start_record)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.btn_end_record = QPushButton(self.widget_5)
        self.btn_end_record.setObjectName(u"btn_end_record")
        self.btn_end_record.setMinimumSize(QSize(120, 20))

        self.horizontalLayout_8.addWidget(self.btn_end_record)


        self.verticalLayout_7.addWidget(self.widget_5)

        self.btn_record_folder = QPushButton(self.widget_2)
        self.btn_record_folder.setObjectName(u"btn_record_folder")
        self.btn_record_folder.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setBold(False)
        font2.setUnderline(False)
        self.btn_record_folder.setFont(font2)

        self.verticalLayout_7.addWidget(self.btn_record_folder)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.record_widget)

        self.transcript_widget = QWidget(self.settings_widget)
        self.transcript_widget.setObjectName(u"transcript_widget")
        self.transcript_widget.setStyleSheet(u"background: #ffeaeb;\n"
"border-radius: 5px;\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.transcript_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.transcript_label = QLabel(self.transcript_widget)
        self.transcript_label.setObjectName(u"transcript_label")
        self.transcript_label.setMinimumSize(QSize(0, 40))
        self.transcript_label.setMaximumSize(QSize(16777215, 40))
        self.transcript_label.setFont(font1)

        self.verticalLayout_5.addWidget(self.transcript_label)

        self.widget_3 = QWidget(self.transcript_widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QPushButton {\n"
"	border-radius : 9px;\n"
"	minimum-height : 30px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	background : #ffbfc0;\n"
"}\n"
"QPushButton::hover {\n"
"	background : #ffffff;\n"
"}\n"
"QPushButton::pressed {\n"
"	background : #ffbfc0;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color:red")
        self.label.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label)

        self.select_vocal_widget = QWidget(self.widget_3)
        self.select_vocal_widget.setObjectName(u"select_vocal_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.select_vocal_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_vocal_label = QLabel(self.select_vocal_widget)
        self.select_vocal_label.setObjectName(u"select_vocal_label")

        self.horizontalLayout_2.addWidget(self.select_vocal_label)

        self.vocal_file_path = QLineEdit(self.select_vocal_widget)
        self.vocal_file_path.setObjectName(u"vocal_file_path")
        self.vocal_file_path.setMinimumSize(QSize(120, 0))
        self.vocal_file_path.setStyleSheet(u"background: #EDD3DC")
        self.vocal_file_path.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.vocal_file_path)

        self.btn_select_vocal = QPushButton(self.select_vocal_widget)
        self.btn_select_vocal.setObjectName(u"btn_select_vocal")
        self.btn_select_vocal.setMinimumSize(QSize(70, 18))

        self.horizontalLayout_2.addWidget(self.btn_select_vocal)


        self.verticalLayout_8.addWidget(self.select_vocal_widget)

        self.select_model_widget = QWidget(self.widget_3)
        self.select_model_widget.setObjectName(u"select_model_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.select_model_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.select_model_label = QLabel(self.select_model_widget)
        self.select_model_label.setObjectName(u"select_model_label")

        self.horizontalLayout_3.addWidget(self.select_model_label)

        self.model_file_path = QLineEdit(self.select_model_widget)
        self.model_file_path.setObjectName(u"model_file_path")
        self.model_file_path.setMinimumSize(QSize(120, 0))
        self.model_file_path.setStyleSheet(u"background: #EDD3DC")
        self.model_file_path.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.model_file_path)

        self.btn_select_model = QPushButton(self.select_model_widget)
        self.btn_select_model.setObjectName(u"btn_select_model")
        self.btn_select_model.setMinimumSize(QSize(70, 18))

        self.horizontalLayout_3.addWidget(self.btn_select_model)


        self.verticalLayout_8.addWidget(self.select_model_widget)

        self.btn_start_trans = QPushButton(self.widget_3)
        self.btn_start_trans.setObjectName(u"btn_start_trans")
        self.btn_start_trans.setMinimumSize(QSize(0, 20))
        font4 = QFont()
        font4.setBold(True)
        self.btn_start_trans.setFont(font4)

        self.verticalLayout_8.addWidget(self.btn_start_trans)

        self.btn_trans_and_minutes = QPushButton(self.widget_3)
        self.btn_trans_and_minutes.setObjectName(u"btn_trans_and_minutes")
        self.btn_trans_and_minutes.setMinimumSize(QSize(0, 20))
        self.btn_trans_and_minutes.setFont(font4)

        self.verticalLayout_8.addWidget(self.btn_trans_and_minutes)

        self.btn_trans_folder = QPushButton(self.widget_3)
        self.btn_trans_folder.setObjectName(u"btn_trans_folder")
        self.btn_trans_folder.setMinimumSize(QSize(0, 20))
        font5 = QFont()
        font5.setBold(False)
        self.btn_trans_folder.setFont(font5)
        self.btn_trans_folder.setStyleSheet(u"color: black")

        self.verticalLayout_8.addWidget(self.btn_trans_folder)

        self.btn_model_folder = QPushButton(self.widget_3)
        self.btn_model_folder.setObjectName(u"btn_model_folder")
        self.btn_model_folder.setMinimumSize(QSize(0, 20))

        self.verticalLayout_8.addWidget(self.btn_model_folder)


        self.verticalLayout_5.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.transcript_widget)

        self.minute_widget = QWidget(self.settings_widget)
        self.minute_widget.setObjectName(u"minute_widget")
        self.minute_widget.setStyleSheet(u"background: #ffeaeb;\n"
"border-radius: 5px;")
        self.verticalLayout_6 = QVBoxLayout(self.minute_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.minute_label = QLabel(self.minute_widget)
        self.minute_label.setObjectName(u"minute_label")
        self.minute_label.setMinimumSize(QSize(0, 40))
        self.minute_label.setMaximumSize(QSize(16777215, 40))
        self.minute_label.setFont(font1)

        self.verticalLayout_6.addWidget(self.minute_label)

        self.minute_widget_center = QWidget(self.minute_widget)
        self.minute_widget_center.setObjectName(u"minute_widget_center")
        self.minute_widget_center.setStyleSheet(u"QPushButton {\n"
"	border-radius : 9px;\n"
"	minimum-height : 30px;\n"
"}\n"
"\n"
"/*download*/\n"
"QPushButton {\n"
"	background : #ffbfc0;\n"
"}\n"
"QPushButton::hover {\n"
"	background : #ffffff;\n"
"}\n"
"QPushButton::pressed {\n"
"	background : #ffbfc0;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.minute_widget_center)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_7 = QWidget(self.minute_widget_center)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.api_label = QLabel(self.widget_7)
        self.api_label.setObjectName(u"api_label")

        self.horizontalLayout_5.addWidget(self.api_label)

        self.api_entry = QLineEdit(self.widget_7)
        self.api_entry.setObjectName(u"api_entry")
        self.api_entry.setMinimumSize(QSize(150, 0))
        self.api_entry.setStyleSheet(u"background:white")
        self.api_entry.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_5.addWidget(self.api_entry)

        self.btn_api = QPushButton(self.widget_7)
        self.btn_api.setObjectName(u"btn_api")
        self.btn_api.setMinimumSize(QSize(50, 18))

        self.horizontalLayout_5.addWidget(self.btn_api)


        self.verticalLayout_9.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.minute_widget_center)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.ds_model_label = QLabel(self.widget_8)
        self.ds_model_label.setObjectName(u"ds_model_label")

        self.horizontalLayout_11.addWidget(self.ds_model_label)

        self.ds_model_combobox = QComboBox(self.widget_8)
        self.ds_model_combobox.setObjectName(u"ds_model_combobox")
        self.ds_model_combobox.setStyleSheet(u"background:white")

        self.horizontalLayout_11.addWidget(self.ds_model_combobox)


        self.verticalLayout_9.addWidget(self.widget_8)

        self.widget_6 = QWidget(self.minute_widget_center)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.skill_label = QLabel(self.widget_6)
        self.skill_label.setObjectName(u"skill_label")

        self.horizontalLayout_10.addWidget(self.skill_label)

        self.skill_checkbox = QCheckBox(self.widget_6)
        self.skill_checkbox.setObjectName(u"skill_checkbox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skill_checkbox.sizePolicy().hasHeightForWidth())
        self.skill_checkbox.setSizePolicy(sizePolicy)
        self.skill_checkbox.setMinimumSize(QSize(0, 0))
        self.skill_checkbox.setMaximumSize(QSize(16, 16777215))
        self.skill_checkbox.setStyleSheet(u"background:white; color: black")
        self.skill_checkbox.setChecked(True)

        self.horizontalLayout_10.addWidget(self.skill_checkbox)

        self.btn_open_skill = QPushButton(self.widget_6)
        self.btn_open_skill.setObjectName(u"btn_open_skill")
        self.btn_open_skill.setMinimumSize(QSize(100, 18))
        self.btn_open_skill.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_10.addWidget(self.btn_open_skill)


        self.verticalLayout_9.addWidget(self.widget_6)

        self.widget = QWidget(self.minute_widget_center)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.select_txt_label = QLabel(self.widget)
        self.select_txt_label.setObjectName(u"select_txt_label")

        self.horizontalLayout_6.addWidget(self.select_txt_label)

        self.txt_file_path = QLineEdit(self.widget)
        self.txt_file_path.setObjectName(u"txt_file_path")
        self.txt_file_path.setStyleSheet(u"background: #EDD3DC")
        self.txt_file_path.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.txt_file_path)

        self.btn_select_txt = QPushButton(self.widget)
        self.btn_select_txt.setObjectName(u"btn_select_txt")
        self.btn_select_txt.setMinimumSize(QSize(70, 18))

        self.horizontalLayout_6.addWidget(self.btn_select_txt)


        self.verticalLayout_9.addWidget(self.widget)

        self.btn_minutes = QPushButton(self.minute_widget_center)
        self.btn_minutes.setObjectName(u"btn_minutes")
        self.btn_minutes.setMinimumSize(QSize(0, 20))
        self.btn_minutes.setFont(font4)

        self.verticalLayout_9.addWidget(self.btn_minutes)

        self.btn_minute_folder = QPushButton(self.minute_widget_center)
        self.btn_minute_folder.setObjectName(u"btn_minute_folder")
        self.btn_minute_folder.setMinimumSize(QSize(0, 20))
        self.btn_minute_folder.setFont(font5)

        self.verticalLayout_9.addWidget(self.btn_minute_folder)

        self.btn_ds_open_web = QPushButton(self.minute_widget_center)
        self.btn_ds_open_web.setObjectName(u"btn_ds_open_web")
        self.btn_ds_open_web.setMinimumSize(QSize(0, 20))

        self.verticalLayout_9.addWidget(self.btn_ds_open_web)


        self.verticalLayout_6.addWidget(self.minute_widget_center)


        self.horizontalLayout.addWidget(self.minute_widget)


        self.verticalLayout.addWidget(self.settings_widget)

        self.result_widget = QWidget(self.centralwidget)
        self.result_widget.setObjectName(u"result_widget")
        self.result_widget.setStyleSheet(u"background: #ffe0e1;\n"
"border-radius: 15px;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.result_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(18, 18, 18, 18)
        self.console_label_widget = QWidget(self.result_widget)
        self.console_label_widget.setObjectName(u"console_label_widget")
        self.console_label_widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.console_label_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.console_label = QLabel(self.console_label_widget)
        self.console_label.setObjectName(u"console_label")
        self.console_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.console_label)


        self.verticalLayout_3.addWidget(self.console_label_widget)

        self.console_text = QTextEdit(self.result_widget)
        self.console_text.setObjectName(u"console_text")
        self.console_text.setStyleSheet(u"background: #EDD3DC;\n"
"padding :5px;")

        self.verticalLayout_3.addWidget(self.console_text)


        self.verticalLayout.addWidget(self.result_widget)

        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setBold(False)
        self.name_label.setFont(font6)
        self.name_label.setStyleSheet(u"color : #C76E8D")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.name_label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AfterTalk", None))
        self.topic_label.setText(QCoreApplication.translate("MainWindow", u"AfterTalk", None))
        self.topic_two.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u672c\u5730\u6a21\u578b + Deepseek SDK \u7684\u4f1a\u8bae\u7eaa\u8981\u5de5\u5177", None))
        self.record_label.setText(QCoreApplication.translate("MainWindow", u"  \u5f55\u97f3\u8bbe\u5b9a", None))
        self.timer_label.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u65f6", None))
        self.timer_show.setDisplayFormat(QCoreApplication.translate("MainWindow", u"H:mm:ss", None))
        self.rename_file_label.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u6587\u4ef6\u547d\u540d", None))
        self.rename_file_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u662f\u65e5\u671f\u65f6\u95f4\uff0c\u4e0d\u9700\u8981\u8f93\u5165\u6587\u4ef6\u540e\u7f00", None))
        self.btn_start_record.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u97f3", None))
        self.btn_end_record.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u5f55\u97f3", None))
        self.btn_record_folder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5f55\u97f3\u6587\u4ef6\u5939", None))
        self.transcript_label.setText(QCoreApplication.translate("MainWindow", u"  \u4f1a\u8bae\u5e95\u7a3f\u8f6c\u5f55\u8bbe\u5b9a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a\u8f6c\u5f55\u9700\u8981\u4f7f\u7528\u7a7a\u95f2CPU\u7ebf\u7a0b\uff0c\u8bf7\u786e\u4fdd\u8bbe\u5907\u6563\u70ed\u6b63\u5e38\u3002\u6a21\u578b\u5927\u5c0f\u51b3\u5b9a\u51c6\u786e\u5ea6\u548c\u8f6c\u5f55\u901f\u5ea6\uff0ctiny\u6700\u5feb\u4f46\u662f\u51c6\u5ea6\u5dee\uff0cmedium\u51c6\u5ea6\u5f88\u9ad8\u4f4610\u5206\u949f\u4f1a\u8bae\u5927\u7ea6\u9700\u89815\u5206\u949f\u8f6c\u5f55\uff0c\u8bf7\u81ea\u884c\u9009\u62e9\u5408\u9002\u6a21\u578b\u3002", None))
        self.select_vocal_label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u97f3\u9891\u6587\u4ef6", None))
        self.vocal_file_path.setText("")
        self.vocal_file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recording file path", None))
        self.btn_select_vocal.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.select_model_label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u672c\u5730\u6a21\u578b\u6587\u4ef6", None))
        self.model_file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Model file path", None))
        self.btn_select_model.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.btn_start_trans.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u5f55\u5e95\u7a3f", None))
        self.btn_trans_and_minutes.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u8f6c\u5f55\u5e95\u7a3f+\u6574\u7406\u4f1a\u8bae\u7eaa\u8981", None))
        self.btn_trans_folder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4f1a\u8bae\u5e95\u7a3f\u6587\u4ef6\u5939", None))
        self.btn_model_folder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6a21\u578b\u6587\u4ef6\u5939", None))
        self.minute_label.setText(QCoreApplication.translate("MainWindow", u"  \u4f1a\u8bae\u7eaa\u8981\u751f\u6210\u8bbe\u5b9a", None))
        self.api_label.setText(QCoreApplication.translate("MainWindow", u"Deepseek API Key", None))
        self.api_entry.setInputMask("")
        self.api_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165Deepseek API KEY", None))
        self.btn_api.setText(QCoreApplication.translate("MainWindow", u"\u4f20\u5165", None))
        self.ds_model_label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9Deepseek\u6a21\u578b", None))
        self.skill_label.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4f20\u5165skill\u6587\u6863\u8f85\u52a9\u751f\u6210", None))
        self.skill_checkbox.setText("")
        self.btn_open_skill.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91skill\u6587\u4ef6", None))
        self.select_txt_label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5e95\u7a3f\u6587\u4ef6(.txt file)", None))
        self.txt_file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u".txt file path", None))
        self.btn_select_txt.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.btn_minutes.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u751f\u6210\u4f1a\u8bae\u7eaa\u8981", None))
        self.btn_minute_folder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4f1a\u8bae\u7eaa\u8981\u6587\u4ef6\u5939", None))
        self.btn_ds_open_web.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u5668\u6253\u5f00Deepseek API\u7ba1\u7406\u754c\u9762", None))
        self.console_label.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u8fdb\u5ea6\u4e0e\u63a7\u5236\u53f0\u4fe1\u606f", None))
        self.console_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Console\u6587\u672c\u4e0e\u4efb\u52a1\u8fdb\u5ea6\u4f1a\u663e\u793a\u5728\u6b64", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Established by - Kitazaki Hinata", None))
    # retranslateUi

