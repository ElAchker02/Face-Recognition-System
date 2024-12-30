# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserCRUD.ui'
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
        MainWindow.resize(420, 340)
        MainWindow.setMinimumSize(QSize(420, 340))
        MainWindow.setMaximumSize(QSize(420, 340))
        MainWindow.setStyleSheet(u"background-color: rgb(254, 254, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(120, 110, 179, 22))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.splitter_2.addWidget(self.label_2)
        self.txtphotoPath = QLineEdit(self.splitter_2)
        self.txtphotoPath.setObjectName(u"txtphotoPath")
        self.splitter_2.addWidget(self.txtphotoPath)
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(120, 160, 179, 22))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.splitter_3.addWidget(self.label_3)
        self.cmbDep = QComboBox(self.splitter_3)
        self.cmbDep.setObjectName(u"cmbDep")
        self.splitter_3.addWidget(self.cmbDep)
        self.splitter_4 = QSplitter(self.centralwidget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(120, 200, 179, 22))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.splitter_4.addWidget(self.label_4)
        self.cmbRole = QComboBox(self.splitter_4)
        self.cmbRole.addItem("")
        self.cmbRole.addItem("")
        self.cmbRole.setObjectName(u"cmbRole")
        self.splitter_4.addWidget(self.cmbRole)
        self.btnConfUser = QPushButton(self.centralwidget)
        self.btnConfUser.setObjectName(u"btnConfUser")
        self.btnConfUser.setGeometry(QRect(160, 250, 93, 28))
        self.btnConfUser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(120, 60, 179, 22))
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label)
        self.txtName = QLineEdit(self.splitter)
        self.txtName.setObjectName(u"txtName")
        self.splitter.addWidget(self.txtName)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Photo path :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Departement :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Role :", None))
        self.cmbRole.setItemText(0, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.cmbRole.setItemText(1, QCoreApplication.translate("MainWindow", u"Employee", None))

        self.btnConfUser.setText(QCoreApplication.translate("MainWindow", u"Confirmer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
    # retranslateUi

