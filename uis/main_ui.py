# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1078, 719)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.title_frame)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title)

        self.title2 = QLabel(self.title_frame)
        self.title2.setObjectName(u"title2")

        self.horizontalLayout.addWidget(self.title2)

        self.pushButton = QPushButton(self.title_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.title_frame, 0, 0, 1, 2)

        self.listWidget_icon = QListWidget(self.centralwidget)
        self.listWidget_icon.setObjectName(u"listWidget_icon")
        self.listWidget_icon.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.listWidget_icon, 1, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label = QLabel(self.dashboard_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 190, 161, 20))
        self.stackedWidget.addWidget(self.dashboard_page)
        self.Users_page = QWidget()
        self.Users_page.setObjectName(u"Users_page")
        self.label_2 = QLabel(self.Users_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 210, 111, 16))
        self.stackedWidget.addWidget(self.Users_page)
        self.logs_page = QWidget()
        self.logs_page.setObjectName(u"logs_page")
        self.label_3 = QLabel(self.logs_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 230, 111, 16))
        self.stackedWidget.addWidget(self.logs_page)
        self.departements_page = QWidget()
        self.departements_page.setObjectName(u"departements_page")
        self.label_6 = QLabel(self.departements_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 80, 131, 16))
        self.stackedWidget.addWidget(self.departements_page)
        self.admins_page = QWidget()
        self.admins_page.setObjectName(u"admins_page")
        self.label_5 = QLabel(self.admins_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 160, 55, 16))
        self.stackedWidget.addWidget(self.admins_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_4 = QLabel(self.settings_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 120, 55, 16))
        self.stackedWidget.addWidget(self.settings_page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 4, 1, 1)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.admin = QLabel(self.frame_2)
        self.admin.setObjectName(u"admin")

        self.horizontalLayout_2.addWidget(self.admin)

        self.timestamps = QLabel(self.frame_2)
        self.timestamps.setObjectName(u"timestamps")

        self.horizontalLayout_2.addWidget(self.timestamps)


        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.title2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"dashboard", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Users Page", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logs Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"departements", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"admins", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.admin.setText(QCoreApplication.translate("MainWindow", u"Amine", None))
        self.timestamps.setText(QCoreApplication.translate("MainWindow", u"timestamps", None))
    # retranslateUi

