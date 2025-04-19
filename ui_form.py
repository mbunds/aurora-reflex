# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1191, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: rgb(112, 112, 112);\n"
"}")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionLaunch_Browser = QAction(MainWindow)
        self.actionLaunch_Browser.setObjectName(u"actionLaunch_Browser")
        self.actionLaunch_Terminal = QAction(MainWindow)
        self.actionLaunch_Terminal.setObjectName(u"actionLaunch_Terminal")
        self.actionLaunch_SQLite_Editor = QAction(MainWindow)
        self.actionLaunch_SQLite_Editor.setObjectName(u"actionLaunch_SQLite_Editor")
        self.actionExport_Sequence = QAction(MainWindow)
        self.actionExport_Sequence.setObjectName(u"actionExport_Sequence")
        self.actionImport_Sequence = QAction(MainWindow)
        self.actionImport_Sequence.setObjectName(u"actionImport_Sequence")
        self.actionNew_Sequence = QAction(MainWindow)
        self.actionNew_Sequence.setObjectName(u"actionNew_Sequence")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tw_aurora = QTabWidget(self.centralwidget)
        self.tw_aurora.setObjectName(u"tw_aurora")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tw_aurora.sizePolicy().hasHeightForWidth())
        self.tw_aurora.setSizePolicy(sizePolicy1)
        self.tw_aurora.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(True)
        self.tw_aurora.setFont(font)
        self.tw_aurora.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"	background: #4c4c4c;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #4c4c4c;\n"
"    color: #ccc;\n"
"    padding: 6px 12px;\n"
"    border: 1px solid #555;\n"
"    border-bottom: none;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #3e3efe;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #2a2a2a;\n"
"}\n"
"")
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        sizePolicy.setHeightForWidth(self.tab_home.sizePolicy().hasHeightForWidth())
        self.tab_home.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.tab_home)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_aurora_large = QLabel(self.tab_home)
        self.lbl_aurora_large.setObjectName(u"lbl_aurora_large")
        sizePolicy.setHeightForWidth(self.lbl_aurora_large.sizePolicy().hasHeightForWidth())
        self.lbl_aurora_large.setSizePolicy(sizePolicy)
        self.lbl_aurora_large.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.lbl_aurora_large, 0, 0, 1, 1)

        self.tw_aurora.addTab(self.tab_home, "")
        self.tab_actions = QWidget()
        self.tab_actions.setObjectName(u"tab_actions")
        sizePolicy.setHeightForWidth(self.tab_actions.sizePolicy().hasHeightForWidth())
        self.tab_actions.setSizePolicy(sizePolicy)
        self.tab_actions.setFont(font)
        self.tab_actions.setStyleSheet(u"alternate-background-color: rgb(59, 59, 59);")
        self.tw_aurora.addTab(self.tab_actions, "")
        self.tab_sequencer = QWidget()
        self.tab_sequencer.setObjectName(u"tab_sequencer")
        sizePolicy.setHeightForWidth(self.tab_sequencer.sizePolicy().hasHeightForWidth())
        self.tab_sequencer.setSizePolicy(sizePolicy)
        self.tab_sequencer.setFont(font)
        self.tab_sequencer.setAutoFillBackground(False)
        self.tab_sequencer.setStyleSheet(u"alternate-background-color: rgb(59, 59, 59);")
        self.gridLayout_2 = QGridLayout(self.tab_sequencer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_sequence_arm = QPushButton(self.tab_sequencer)
        self.pb_sequence_arm.setObjectName(u"pb_sequence_arm")
        self.pb_sequence_arm.setFont(font)
        self.pb_sequence_arm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_sequence_arm.setStyleSheet(u"background-color: rgb(75 75, 75);")
        self.pb_sequence_arm.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.pb_sequence_arm, 1, 1, 1, 1)

        self.lv_sequences = QListView(self.tab_sequencer)
        self.lv_sequences.setObjectName(u"lv_sequences")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lv_sequences.sizePolicy().hasHeightForWidth())
        self.lv_sequences.setSizePolicy(sizePolicy2)
        self.lv_sequences.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.lv_sequences.setStyleSheet(u"QListView {\n"
"    background-color: #1e1e1e;\n"
"    color: #ffff90;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.lv_sequences, 1, 0, 3, 1)

        self.lv_steps = QListView(self.tab_sequencer)
        self.lv_steps.setObjectName(u"lv_steps")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lv_steps.sizePolicy().hasHeightForWidth())
        self.lv_steps.setSizePolicy(sizePolicy3)
        self.lv_steps.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.lv_steps.setStyleSheet(u"QListView {\n"
"    background-color: #1e1e1e;\n"
"    color: #ffffff;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.lv_steps, 6, 0, 1, 1)

        self.lbl_sequence = QLabel(self.tab_sequencer)
        self.lbl_sequence.setObjectName(u"lbl_sequence")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbl_sequence.setFont(font1)
        self.lbl_sequence.setStyleSheet(u"color: rgb(128, 128, 255);")

        self.gridLayout_2.addWidget(self.lbl_sequence, 0, 0, 1, 1)

        self.pb_sequence_edit = QPushButton(self.tab_sequencer)
        self.pb_sequence_edit.setObjectName(u"pb_sequence_edit")
        self.pb_sequence_edit.setEnabled(False)
        self.pb_sequence_edit.setFont(font)
        self.pb_sequence_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_sequence_edit.setStyleSheet(u"background-color: rgb(75 75, 75);")

        self.gridLayout_2.addWidget(self.pb_sequence_edit, 3, 1, 1, 1)

        self.pb_sequence_run = QPushButton(self.tab_sequencer)
        self.pb_sequence_run.setObjectName(u"pb_sequence_run")
        self.pb_sequence_run.setEnabled(False)
        self.pb_sequence_run.setFont(font)
        self.pb_sequence_run.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pb_sequence_run.setStyleSheet(u"background-color: rgb(75 75, 75);")

        self.gridLayout_2.addWidget(self.pb_sequence_run, 2, 1, 1, 1)

        self.lbl_steps = QLabel(self.tab_sequencer)
        self.lbl_steps.setObjectName(u"lbl_steps")
        self.lbl_steps.setFont(font1)
        self.lbl_steps.setStyleSheet(u"color: rgb(128, 128, 255);")

        self.gridLayout_2.addWidget(self.lbl_steps, 4, 0, 1, 1)

        self.tw_aurora.addTab(self.tab_sequencer, "")

        self.gridLayout.addWidget(self.tw_aurora, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1191, 21))
        self.menubar.setStyleSheet(u"QMenuBar{\n"
"	color: rgb(170, 255, 0);\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionNew_Sequence)
        self.menuEdit.addAction(self.actionImport_Sequence)
        self.menuEdit.addAction(self.actionExport_Sequence)
        self.menuTools.addAction(self.actionLaunch_Browser)
        self.menuTools.addAction(self.actionLaunch_Terminal)
        self.menuTools.addAction(self.actionLaunch_SQLite_Editor)

        self.retranslateUi(MainWindow)

        self.tw_aurora.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AURORA V1.0", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionLaunch_Browser.setText(QCoreApplication.translate("MainWindow", u"Launch Browser", None))
        self.actionLaunch_Terminal.setText(QCoreApplication.translate("MainWindow", u"Launch Terminal", None))
        self.actionLaunch_SQLite_Editor.setText(QCoreApplication.translate("MainWindow", u"Launch SQLite Editor", None))
        self.actionExport_Sequence.setText(QCoreApplication.translate("MainWindow", u"Export Sequence", None))
        self.actionImport_Sequence.setText(QCoreApplication.translate("MainWindow", u"Import Sequence", None))
        self.actionNew_Sequence.setText(QCoreApplication.translate("MainWindow", u"New Sequence", None))
#if QT_CONFIG(tooltip)
        self.tw_aurora.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbl_aurora_large.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tw_aurora.setTabText(self.tw_aurora.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"AURORA", None))
        self.tw_aurora.setTabText(self.tw_aurora.indexOf(self.tab_actions), QCoreApplication.translate("MainWindow", u"ACTIONS", None))
#if QT_CONFIG(tooltip)
        self.pb_sequence_arm.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pb_sequence_arm.setText(QCoreApplication.translate("MainWindow", u"ARM", None))
        self.lbl_sequence.setText(QCoreApplication.translate("MainWindow", u"SEQUENCES", None))
        self.pb_sequence_edit.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.pb_sequence_run.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.lbl_steps.setText(QCoreApplication.translate("MainWindow", u"STEPS", None))
        self.tw_aurora.setTabText(self.tw_aurora.indexOf(self.tab_sequencer), QCoreApplication.translate("MainWindow", u"SEQUENCER", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

