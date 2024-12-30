# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminsCRUD.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 320)
        MainWindow.setMinimumSize(QSize(420, 320))
        MainWindow.setMaximumSize(QSize(420, 320))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(110, 90, 179, 22))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.splitter_2.addWidget(self.label_2)
        self.txtemail = QLineEdit(self.splitter_2)
        self.txtemail.setObjectName(u"txtemail")
        self.splitter_2.addWidget(self.txtemail)
        self.splitter_4 = QSplitter(self.centralwidget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(110, 190, 179, 22))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.btnConfAdmin = QPushButton(self.splitter_4)
        self.btnConfAdmin.setObjectName(u"btnConfAdmin")
        self.btnConfAdmin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.splitter_4.addWidget(self.btnConfAdmin)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(110, 50, 179, 22))
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter_3 = QSplitter(self.splitter)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.splitter_3.addWidget(self.label_3)
        self.cmbUsers = QComboBox(self.splitter_3)
        self.cmbUsers.setObjectName(u"cmbUsers")
        self.splitter_3.addWidget(self.cmbUsers)
        self.splitter.addWidget(self.splitter_3)
        self.splitter_5 = QSplitter(self.centralwidget)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(110, 130, 179, 22))
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.splitter_5.addWidget(self.label_4)
        self.txtPassword = QLineEdit(self.splitter_5)
        self.txtPassword.setObjectName(u"txtPassword")
        self.splitter_5.addWidget(self.txtPassword)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
        self.btnConfAdmin.setText(QCoreApplication.translate("MainWindow", u"Confirmer", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
    # retranslateUi

