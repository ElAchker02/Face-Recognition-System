# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DepartementCUD.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
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
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(110, 120, 179, 22))
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label)
        self.txtdep = QLineEdit(self.splitter)
        self.txtdep.setObjectName(u"txtdep")
        self.splitter.addWidget(self.txtdep)
        self.btnConfDep = QPushButton(self.centralwidget)
        self.btnConfDep.setObjectName(u"btnConfDep")
        self.btnConfDep.setGeometry(QRect(150, 230, 93, 28))
        self.btnConfDep.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 420, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Departement :", None))
        self.btnConfDep.setText(QCoreApplication.translate("MainWindow", u"Confirmer", None))
    # retranslateUi

