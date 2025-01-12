from PyQt6 import QtCore, QtGui, QtWidgets

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem,QWidget, QGridLayout,QMessageBox,QFileDialog
from PyQt6.QtCore import Qt, QSize,QSortFilterProxyModel,QTimer
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtCore import QPropertyAnimation
from db_operations import DatabaseManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from UserCRUD import UserCRUDWindow
from DepartementCRUD import DepartementCRUDWindow
from AdminsCRUD import AdminCRUDWindow
import pandas as pd
import xlsxwriter
from datetime import datetime
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1581, 844)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)
        self.listWidget_icon = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_icon.setMaximumSize(QtCore.QSize(50, 16777215))
        self.listWidget_icon.setObjectName("listWidget_icon")
        self.gridLayout.addWidget(self.listWidget_icon, 1, 0, 1, 1)
        self.title_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.title_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_frame.setObjectName("title_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title = QtWidgets.QLabel(parent=self.title_frame)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.title2 = QtWidgets.QLabel(parent=self.title_frame)
        self.title2.setObjectName("title2")
        self.horizontalLayout.addWidget(self.title2)
        self.pushButton = QtWidgets.QPushButton(parent=self.title_frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.title_frame, 0, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.admin = QtWidgets.QLabel(parent=self.frame_2)
        self.admin.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.admin.setObjectName("admin")
        self.horizontalLayout_2.addWidget(self.admin)
        self.timestamps = QtWidgets.QLabel(parent=self.frame_2)
        self.timestamps.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.timestamps.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.timestamps.setObjectName("timestamps")
        self.horizontalLayout_2.addWidget(self.timestamps)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 2)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboard_page = QtWidgets.QWidget()
        self.dashboard_page.setObjectName("dashboard_page")
        self.widget = QtWidgets.QWidget(parent=self.dashboard_page)
        self.widget.setGeometry(QtCore.QRect(30, 60, 1251, 521))
        self.widget.setObjectName("widget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_9.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nbUsers = QtWidgets.QLabel(parent=self.groupBox)
        self.nbUsers.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nbUsers.setObjectName("nbUsers")
        self.gridLayout_3.addWidget(self.nbUsers, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.entriesToday = QtWidgets.QLabel(parent=self.groupBox_3)
        self.entriesToday.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.entriesToday.setObjectName("entriesToday")
        self.gridLayout_5.addWidget(self.entriesToday, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.nbUnrecognizedToday = QtWidgets.QLabel(parent=self.groupBox_2)
        self.nbUnrecognizedToday.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nbUnrecognizedToday.setObjectName("nbUnrecognizedToday")
        self.gridLayout_4.addWidget(self.nbUnrecognizedToday, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.nbRecognizedPersons = QtWidgets.QLabel(parent=self.groupBox_4)
        self.nbRecognizedPersons.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nbRecognizedPersons.setObjectName("nbRecognizedPersons")
        self.gridLayout_6.addWidget(self.nbRecognizedPersons, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_4, 0, 3, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.wrongPrediction = QtWidgets.QLabel(parent=self.groupBox_5)
        self.wrongPrediction.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wrongPrediction.setObjectName("wrongPrediction")
        self.gridLayout_7.addWidget(self.wrongPrediction, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 1, 0, 1, 2)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.truePredictions = QtWidgets.QLabel(parent=self.groupBox_6)
        self.truePredictions.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.truePredictions.setObjectName("truePredictions")
        self.gridLayout_8.addWidget(self.truePredictions, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_6, 1, 2, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.entrieslast7 = QtWidgets.QLabel(parent=self.groupBox_7)
        self.entrieslast7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.entrieslast7.setObjectName("entrieslast7")
        self.gridLayout_10.addWidget(self.entrieslast7, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_7, 1, 3, 1, 1)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.Users_page = QtWidgets.QWidget()
        self.Users_page.setObjectName("Users_page")
        self.tableUsers = QtWidgets.QTableWidget(parent=self.Users_page)
        self.tableUsers.setGeometry(QtCore.QRect(10, 80, 1271, 571))
        self.tableUsers.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableUsers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableUsers.setObjectName("tableUsers")
        self.tableUsers.setColumnCount(5)
        self.tableUsers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(4, item)
        self.frame_6 = QtWidgets.QFrame(parent=self.Users_page)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1301, 88))
        self.frame_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 42, 21))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(147, 30, 83, 21))
        self.label_7.setObjectName("label_7")
        self.txtUser = QtWidgets.QLineEdit(parent=self.frame_6)
        self.txtUser.setGeometry(QtCore.QRect(350, 30, 171, 27))
        self.txtUser.setObjectName("txtUser")
        self.cmbUsers = QtWidgets.QComboBox(parent=self.frame_6)
        self.cmbUsers.setGeometry(QtCore.QRect(252, 30, 87, 27))
        self.cmbUsers.setObjectName("cmbUsers")
        self.cmbUsers.addItem("")
        self.cmbUsers.addItem("")
        self.cmbUsers.addItem("")
        self.cmbUsers.addItem("")
        self.btnAddUser = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnAddUser.setGeometry(QtCore.QRect(593, 30, 93, 30))
        self.btnAddUser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\uis\\../icon/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAddUser.setIcon(icon)
        self.btnAddUser.setObjectName("btnAddUser")
        self.btnRefreshUser = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnRefreshUser.setGeometry(QtCore.QRect(10, 30, 41, 30))
        self.btnRefreshUser.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btnRefreshUser.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\uis\\../icon/ref.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnRefreshUser.setIcon(icon1)
        self.btnRefreshUser.setObjectName("btnRefreshUser")
        self.btnExportUser = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnExportUser.setGeometry(QtCore.QRect(1180, 30, 93, 30))
        self.btnExportUser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\uis\\../icon/export.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnExportUser.setIcon(icon2)
        self.btnExportUser.setObjectName("btnExportUser")
        self.btnSearchUsers = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnSearchUsers.setGeometry(QtCore.QRect(530, 30, 41, 30))
        self.btnSearchUsers.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnSearchUsers.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\uis\\../icon/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSearchUsers.setIcon(icon3)
        self.btnSearchUsers.setObjectName("btnSearchUsers")
        self.btnUpdateUser = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnUpdateUser.setGeometry(QtCore.QRect(720, 30, 93, 30))
        self.btnUpdateUser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\uis\\../icon/updae.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnUpdateUser.setIcon(icon4)
        self.btnUpdateUser.setObjectName("btnUpdateUser")
        self.btnRmoveUser = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnRmoveUser.setGeometry(QtCore.QRect(850, 30, 93, 30))
        self.btnRmoveUser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\uis\\../icon/trash.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnRmoveUser.setIcon(icon5)
        self.btnRmoveUser.setObjectName("btnRmoveUser")
        self.stackedWidget.addWidget(self.Users_page)
        self.logs_page = QtWidgets.QWidget()
        self.logs_page.setObjectName("logs_page")
        self.frame_3 = QtWidgets.QFrame(parent=self.logs_page)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1281, 88))
        self.frame_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 42, 21))
        self.label_3.setObjectName("label_3")
        self.bntRefreshLogs = QtWidgets.QPushButton(parent=self.frame_3)
        self.bntRefreshLogs.setGeometry(QtCore.QRect(10, 30, 41, 30))
        self.bntRefreshLogs.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.bntRefreshLogs.setText("")
        self.bntRefreshLogs.setIcon(icon1)
        self.bntRefreshLogs.setObjectName("bntRefreshLogs")
        self.btnExportLogs = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnExportLogs.setGeometry(QtCore.QRect(1180, 30, 93, 30))
        self.btnExportLogs.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExportLogs.setIcon(icon2)
        self.btnExportLogs.setObjectName("btnExportLogs")
        self.dateEdit_1 = QtWidgets.QDateEdit(parent=self.frame_3)
        self.dateEdit_1.setGeometry(QtCore.QRect(230, 30, 110, 22))
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.btnSearchLogs = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnSearchLogs.setGeometry(QtCore.QRect(580, 30, 41, 30))
        self.btnSearchLogs.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnSearchLogs.setText("")
        self.btnSearchLogs.setIcon(icon3)
        self.btnSearchLogs.setObjectName("btnSearchLogs")
        self.dateEdit_2 = QtWidgets.QDateEdit(parent=self.frame_3)
        self.dateEdit_2.setGeometry(QtCore.QRect(390, 30, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.tableLogs = QtWidgets.QTableWidget(parent=self.logs_page)
        self.tableLogs.setGeometry(QtCore.QRect(0, 90, 1281, 541))
        self.tableLogs.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableLogs.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableLogs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableLogs.setObjectName("tableLogs")
        self.tableLogs.setColumnCount(4)
        self.tableLogs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(3, item)
        self.stackedWidget.addWidget(self.logs_page)
        self.departements_page = QtWidgets.QWidget()
        self.departements_page.setObjectName("departements_page")
        self.frame_4 = QtWidgets.QFrame(parent=self.departements_page)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1291, 61))
        self.frame_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.btnRefreshDep = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnRefreshDep.setGeometry(QtCore.QRect(12, 12, 33, 29))
        self.btnRefreshDep.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btnRefreshDep.setText("")
        self.btnRefreshDep.setIcon(icon1)
        self.btnRefreshDep.setObjectName("btnRefreshDep")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 250, 30))
        self.label_6.setObjectName("label_6")
        self.tableDepartements = QtWidgets.QTableWidget(parent=self.departements_page)
        self.tableDepartements.setGeometry(QtCore.QRect(0, 90, 1281, 541))
        self.tableDepartements.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableDepartements.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableDepartements.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableDepartements.setObjectName("tableDepartements")
        self.tableDepartements.setColumnCount(2)
        self.tableDepartements.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDepartements.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDepartements.setHorizontalHeaderItem(1, item)
        self.btnUpdateDep = QtWidgets.QPushButton(parent=self.departements_page)
        self.btnUpdateDep.setGeometry(QtCore.QRect(440, 10, 93, 29))
        self.btnUpdateDep.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnUpdateDep.setIcon(icon4)
        self.btnUpdateDep.setObjectName("btnUpdateDep")
        self.btnRemoveDep = QtWidgets.QPushButton(parent=self.departements_page)
        self.btnRemoveDep.setGeometry(QtCore.QRect(564, 10, 93, 29))
        self.btnRemoveDep.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btnRemoveDep.setIcon(icon5)
        self.btnRemoveDep.setObjectName("btnRemoveDep")
        self.btnAddDepartements = QtWidgets.QPushButton(parent=self.departements_page)
        self.btnAddDepartements.setGeometry(QtCore.QRect(689, 10, 93, 29))
        self.btnAddDepartements.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnAddDepartements.setIcon(icon)
        self.btnAddDepartements.setObjectName("btnAddDepartements")
        self.btnExportDepartements = QtWidgets.QPushButton(parent=self.departements_page)
        self.btnExportDepartements.setGeometry(QtCore.QRect(813, 10, 93, 29))
        self.btnExportDepartements.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExportDepartements.setIcon(icon2)
        self.btnExportDepartements.setObjectName("btnExportDepartements")
        self.stackedWidget.addWidget(self.departements_page)
        self.admins_page = QtWidgets.QWidget()
        self.admins_page.setObjectName("admins_page")
        self.frame_5 = QtWidgets.QFrame(parent=self.admins_page)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1281, 88))
        self.frame_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(60, 30, 71, 21))
        self.label_5.setObjectName("label_5")
        self.btnRefeshAdmins = QtWidgets.QPushButton(parent=self.frame_5)
        self.btnRefeshAdmins.setGeometry(QtCore.QRect(0, 30, 33, 29))
        self.btnRefeshAdmins.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btnRefeshAdmins.setText("")
        self.btnRefeshAdmins.setIcon(icon1)
        self.btnRefeshAdmins.setObjectName("btnRefeshAdmins")
        self.layoutWidget = QtWidgets.QWidget(parent=self.frame_5)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 30, 395, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnUpdateAdmin = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnUpdateAdmin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnUpdateAdmin.setIcon(icon4)
        self.btnUpdateAdmin.setObjectName("btnUpdateAdmin")
        self.horizontalLayout_4.addWidget(self.btnUpdateAdmin)
        self.btnRemoveAdmin = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnRemoveAdmin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btnRemoveAdmin.setIcon(icon5)
        self.btnRemoveAdmin.setObjectName("btnRemoveAdmin")
        self.horizontalLayout_4.addWidget(self.btnRemoveAdmin)
        self.btnAddAdmins = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnAddAdmins.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnAddAdmins.setIcon(icon)
        self.btnAddAdmins.setObjectName("btnAddAdmins")
        self.horizontalLayout_4.addWidget(self.btnAddAdmins)
        self.btnExportAdmins = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnExportAdmins.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExportAdmins.setIcon(icon2)
        self.btnExportAdmins.setObjectName("btnExportAdmins")
        self.horizontalLayout_4.addWidget(self.btnExportAdmins)
        self.tableAdmins = QtWidgets.QTableWidget(parent=self.admins_page)
        self.tableAdmins.setGeometry(QtCore.QRect(0, 90, 1281, 621))
        self.tableAdmins.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableAdmins.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableAdmins.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableAdmins.setObjectName("tableAdmins")
        self.tableAdmins.setColumnCount(4)
        self.tableAdmins.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(3, item)
        self.stackedWidget.addWidget(self.admins_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.tableFeddback = QtWidgets.QTableWidget(parent=self.settings_page)
        self.tableFeddback.setGeometry(QtCore.QRect(10, 100, 1281, 541))
        self.tableFeddback.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableFeddback.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableFeddback.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableFeddback.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableFeddback.setObjectName("tableFeddback")
        self.tableFeddback.setColumnCount(4)
        self.tableFeddback.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeddback.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeddback.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeddback.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFeddback.setHorizontalHeaderItem(3, item)
        self.btnRefreshFeedback = QtWidgets.QPushButton(parent=self.settings_page)
        self.btnRefreshFeedback.setGeometry(QtCore.QRect(20, 40, 41, 30))
        self.btnRefreshFeedback.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btnRefreshFeedback.setText("")
        self.btnRefreshFeedback.setIcon(icon1)
        self.btnRefreshFeedback.setObjectName("btnRefreshFeedback")
        self.btnSearchFeedback = QtWidgets.QPushButton(parent=self.settings_page)
        self.btnSearchFeedback.setGeometry(QtCore.QRect(510, 40, 41, 30))
        self.btnSearchFeedback.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnSearchFeedback.setText("")
        self.btnSearchFeedback.setIcon(icon3)
        self.btnSearchFeedback.setObjectName("btnSearchFeedback")
        self.btnExporFeedback = QtWidgets.QPushButton(parent=self.settings_page)
        self.btnExporFeedback.setGeometry(QtCore.QRect(1190, 40, 93, 30))
        self.btnExporFeedback.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExporFeedback.setIcon(icon2)
        self.btnExporFeedback.setObjectName("btnExporFeedback")
        self.label_4 = QtWidgets.QLabel(parent=self.settings_page)
        self.label_4.setGeometry(QtCore.QRect(80, 40, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(parent=self.settings_page)
        self.label_8.setGeometry(QtCore.QRect(240, 40, 121, 16))
        self.label_8.setObjectName("label_8")
        self.cmbFeedback = QtWidgets.QComboBox(parent=self.settings_page)
        self.cmbFeedback.setGeometry(QtCore.QRect(380, 40, 73, 22))
        self.cmbFeedback.setObjectName("cmbFeedback")
        self.cmbFeedback.addItem("")
        self.cmbFeedback.addItem("")
        self.stackedWidget.addWidget(self.settings_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(parent=self.page)
        self.label.setGeometry(QtCore.QRect(560, 0, 231, 101))
        self.label.setStyleSheet("font: 75 30pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.page)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 120, 471, 251))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.txtEmailSender = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.txtEmailSender.setObjectName("txtEmailSender")
        self.gridLayout_2.addWidget(self.txtEmailSender, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.txtPassword = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout_2.addWidget(self.txtPassword, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_11.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.txtEmailReceiver = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.txtEmailReceiver.setObjectName("txtEmailReceiver")
        self.gridLayout_2.addWidget(self.txtEmailReceiver, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_12.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.conf = QtWidgets.QSpinBox(parent=self.layoutWidget1)
        self.conf.setObjectName("conf")
        self.gridLayout_2.addWidget(self.conf, 0, 1, 1, 1)
        self.btnUpdateSettings = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btnUpdateSettings.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnUpdateSettings.setIcon(icon4)
        self.btnUpdateSettings.setObjectName("btnUpdateSettings")
        self.gridLayout_2.addWidget(self.btnUpdateSettings, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1581, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "TextLabel"))
        self.title2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.admin.setText(_translate("MainWindow", "Amine"))
        self.timestamps.setText(_translate("MainWindow", "timestamps"))
        self.groupBox.setTitle(_translate("MainWindow", "Total Users"))
        self.nbUsers.setText(_translate("MainWindow", "0"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Entries Today"))
        self.entriesToday.setText(_translate("MainWindow", "0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Unrecognized Persons Today"))
        self.nbUnrecognizedToday.setText(_translate("MainWindow", "0"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Recognized Persons Today"))
        self.nbRecognizedPersons.setText(_translate("MainWindow", "0"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Number of wrong predictions"))
        self.wrongPrediction.setText(_translate("MainWindow", "0"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Number of true predictions"))
        self.truePredictions.setText(_translate("MainWindow", "0"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Entries Last 7 days"))
        self.entrieslast7.setText(_translate("MainWindow", "0"))
        item = self.tableUsers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableUsers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableUsers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Photo"))
        item = self.tableUsers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Departement"))
        item = self.tableUsers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Role"))
        self.label_2.setText(_translate("MainWindow", "Users"))
        self.label_7.setText(_translate("MainWindow", "Search by :"))
        self.cmbUsers.setItemText(0, _translate("MainWindow", "Id"))
        self.cmbUsers.setItemText(1, _translate("MainWindow", "Name"))
        self.cmbUsers.setItemText(2, _translate("MainWindow", "Departement"))
        self.cmbUsers.setItemText(3, _translate("MainWindow", "Role"))
        self.btnAddUser.setText(_translate("MainWindow", "Add"))
        self.btnExportUser.setText(_translate("MainWindow", "Export"))
        self.btnUpdateUser.setText(_translate("MainWindow", "Update"))
        self.btnRmoveUser.setText(_translate("MainWindow", "Remove"))
        self.label_3.setText(_translate("MainWindow", "Logs"))
        self.btnExportLogs.setText(_translate("MainWindow", "Export"))
        item = self.tableLogs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id log"))
        item = self.tableLogs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "User"))
        item = self.tableLogs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timstamp"))
        item = self.tableLogs.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Emotion"))
        self.label_6.setText(_translate("MainWindow", "Departements"))
        item = self.tableDepartements.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id Departement"))
        item = self.tableDepartements.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Departement Name"))
        self.btnUpdateDep.setText(_translate("MainWindow", "Update"))
        self.btnRemoveDep.setText(_translate("MainWindow", "Remove"))
        self.btnAddDepartements.setText(_translate("MainWindow", "Add"))
        self.btnExportDepartements.setText(_translate("MainWindow", "Export"))
        self.label_5.setText(_translate("MainWindow", "Admins"))
        self.btnUpdateAdmin.setText(_translate("MainWindow", "Update"))
        self.btnRemoveAdmin.setText(_translate("MainWindow", "Remove"))
        self.btnAddAdmins.setText(_translate("MainWindow", "Add"))
        self.btnExportAdmins.setText(_translate("MainWindow", "Export"))
        item = self.tableAdmins.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id Admin"))
        item = self.tableAdmins.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "User"))
        item = self.tableAdmins.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableAdmins.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableFeddback.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id Feedback"))
        item = self.tableFeddback.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id Log"))
        item = self.tableFeddback.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prediction state"))
        item = self.tableFeddback.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Reel User"))
        self.btnExporFeedback.setText(_translate("MainWindow", "Export"))
        self.label_4.setText(_translate("MainWindow", "Feed back"))
        self.label_8.setText(_translate("MainWindow", "Prediction State :"))
        self.cmbFeedback.setItemText(0, _translate("MainWindow", "True"))
        self.cmbFeedback.setItemText(1, _translate("MainWindow", "False"))
        self.label.setText(_translate("MainWindow", "Settings"))
        self.label_9.setText(_translate("MainWindow", "Confidence Tresh hold :"))
        self.label_10.setText(_translate("MainWindow", "Email Sender :"))
        self.label_11.setText(_translate("MainWindow", "Email Receiver :"))
        self.label_12.setText(_translate("MainWindow", "Password :"))
        self.btnUpdateSettings.setText(_translate("MainWindow", "Update"))



class MainWindow(QMainWindow):
    def __init__(self,user_name):
        super().__init__()

        self.user_name = user_name
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize database manager
        self.db_manager = DatabaseManager()

        self.title2 = self.ui.title2
        self.title2.setText("Face Recognition System")

        self.title = self.ui.title
        self.title.setText("")
        self.title.setPixmap(QPixmap("./icon/logo.png"))
        self.title.setScaledContents(True)

        self.side_menu = self.ui.listWidget
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon = self.ui.listWidget_icon
        self.side_menu_icon.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.menu_btn = self.ui.pushButton
        self.menu_btn.setObjectName("menu_btn")
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon("./icon/close.png"))
        self.menu_btn.setIconSize(QSize(30,30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(True)

        self.ui.admin.setText(self.user_name)

        self.side_menu.setHidden(True)
        self.title2.setHidden(True)
        self.title.setHidden(True)
        self.side_menu_icon.setVisible(True)

        # self.side_menu_layout.setContentsMargins(0, 0, 0, 0)
        # self.side_menu_layout.setSpacing(0)

        # self.parent_layout.setContentsMargins(0, 0, 0, 0)

        self.setContentsMargins(0, 0, 0, 0)



        # self.side_menu.setMaximumWidth(200)  # Define the width when visible
        # self.side_menu.setHidden(True)      # Initially hide the sidebar
        # self.side_menu_icon.setMaximumWidth(50)  # Define the width for the icon-only menu



        self.main_content = self.ui.stackedWidget

        self.menu_list = [
            {
                "name":"Dashboard",
                "icon":"./icon/dashboard.png"
            },
                        {
                "name":"Manage Users",
                "icon":"./icon/group.png"
            },
                        {
                "name":"Logs",
                "icon":"./icon/log.png"
            },
                        {
                "name":"Departements",
                "icon":"./icon/department.png"
            },
                        {
                "name":"Admins",
                "icon":"./icon/user.png"
            },
                        {
                "name":"Feed Back",
                "icon":"./icon/feedback.png"
            },
                        {
                "name":"Settings",
                "icon":"./icon/setting.png"
            },
        ]

        self.init_list_widget()
        self.init_signal_slot()
        # self.init_stackwidget()

        # Load dashboard
        self.ui.nbUsers.setText(str(self.db_manager.total_users()))
        self.ui.entriesToday.setText(str(self.db_manager.total_entries_today()))
        self.ui.truePredictions.setText(str(self.db_manager.total_true_predictions()))
        self.ui.wrongPrediction.setText(str(self.db_manager.total_wrong_predictions()))
        self.ui.entrieslast7.setText(str(self.db_manager.total_entries_last_7_days()))
        

        # Load data into tables
        self.load_users_table()
        self.load_admins_table()
        self.load_logs_table()
        self.load_departments_table()
        self.load_feedback_table()
        self.load_settings()

        self.side_menu.setMaximumWidth(0)
        self.side_menu_icon.setMaximumWidth(60)  # Show icon-only menu

        # Timer to update the timestamp
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timestamp)  # Connect the timer signal to the update method
        self.timer.start(1000)  # Update every 1 second

        # Users Actions
        self.ui.btnAddUser.clicked.connect(self.open_user_crud)
        self.ui.btnRefreshUser.clicked.connect(self.load_users_table)
        self.ui.btnRmoveUser.clicked.connect(self.remove_selected_users)
        self.ui.btnUpdateUser.clicked.connect(self.edit_selected_user)

        # Departements Actions
        self.ui.btnRemoveDep.clicked.connect(self.remove_selected_deps)
        self.ui.btnRefreshDep.clicked.connect(self.load_departments_table)
        self.ui.btnAddDepartements.clicked.connect(self.open_dep_crud)
        self.ui.btnUpdateDep.clicked.connect(self.edit_selected_dep)        

        # Admins Actions
        self.ui.btnRemoveAdmin.clicked.connect(self.remove_selected_admins)
        self.ui.btnRefeshAdmins.clicked.connect(self.load_admins_table)
        self.ui.btnAddAdmins.clicked.connect(self.open_admins_crud)
        self.ui.btnUpdateAdmin.clicked.connect(self.edit_selected_admin)  

        # Feed back Actions
        self.ui.btnRefreshFeedback.clicked.connect(self.load_feedback_table)

        # Excel Export Actions
        self.ui.btnExportUser.clicked.connect(lambda: self.export_table_to_excel(self.ui.tableUsers))
        self.ui.btnExportLogs.clicked.connect(lambda: self.export_table_to_excel(self.ui.tableLogs))
        self.ui.btnExportAdmins.clicked.connect(lambda: self.export_table_to_excel(self.ui.tableAdmins))
        self.ui.btnExportDepartements.clicked.connect(lambda: self.export_table_to_excel(self.ui.tableDepartements))
        self.ui.btnExporFeedback.clicked.connect(lambda: self.export_table_to_excel(self.ui.tableFeddback))

        # settings
        self.ui.btnUpdateSettings.clicked.connect(self.update_settings)

        # Research Buttons
        self.ui.btnSearchUsers.clicked.connect(self.user_search)
        # self.ui.btnSearchLogs.clicked.connect(self.logs_search)
        self.ui.btnSearchFeedback.clicked.connect(self.feed_back_search)
        
    def init_signal_slot(self):
        self.menu_btn.toggled["bool"].connect(self.side_menu.setHidden)
        self.menu_btn.toggled["bool"].connect(self.title2.setHidden)
        self.menu_btn.toggled["bool"].connect(self.title.setHidden)
        self.menu_btn.toggled["bool"].connect(self.side_menu_icon.setVisible)

        # self.side_menu.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        # self.side_menu_icon.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        # self.side_menu.currentRowChanged["int"].connect(self.side_menu_icon.setCurrentIndex)
        # self.side_menu_icon.currentRowChanged["int"].connect(self.side_menu.setCurrentRow)

        self.side_menu.currentRowChanged.connect(self.main_content.setCurrentIndex)
        self.side_menu_icon.currentRowChanged.connect(self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged.connect(self.side_menu_icon.setCurrentRow)
        self.side_menu_icon.currentRowChanged.connect(self.side_menu.setCurrentRow)





        self.menu_btn.toggled.connect(self.button_icon_change)

    def update_timestamp(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.timestamps.setText(f"{current_time}")


    def export_table_to_excel(self, table_widget):
        try:
            # Open file dialog to select the save location
            file_path, _ = QFileDialog.getSaveFileName(
                None, 
                "Save File", 
                "", 
                "Excel Files (*.xlsx)"
            )
            if not file_path:  # If the user cancels the dialog, exit the function
                return

            # Add ".xlsx" extension if not provided
            if not file_path.endswith('.xlsx'):
                file_path += '.xlsx'

            # Create an Excel workbook and worksheet
            workbook = xlsxwriter.Workbook(file_path)
            worksheet = workbook.add_worksheet()

            # Write the table headers
            for col in range(table_widget.columnCount()):
                header = table_widget.horizontalHeaderItem(col).text()
                worksheet.write(0, col, header)

            # Write the table data
            for row in range(table_widget.rowCount()):
                for col in range(table_widget.columnCount()):
                    cell_item = table_widget.item(row, col)
                    if cell_item is not None:
                        worksheet.write(row + 1, col, cell_item.text())

            workbook.close()  # Save the workbook

            # Show a success message
            QMessageBox.information(None, "Success", f"Table exported successfully to {file_path}!")

        except Exception as e:
            # Show an error message if something goes wrong
            QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")

    def animate_sidebar(self, expand):
        if expand:  # Expand the sidebar
            self.animation = QPropertyAnimation(self.side_menu, b"maximumWidth")
            self.animation.setDuration(300)  # Animation duration in milliseconds
            self.animation.setStartValue(0)
            self.animation.setEndValue(250)  # Full sidebar width
            self.animation.start()

            self.icon_animation = QPropertyAnimation(self.side_menu_icon, b"maximumWidth")
            self.icon_animation.setDuration(300)
            self.icon_animation.setStartValue(50)
            self.icon_animation.setEndValue(0) # Hide icon-only menu
            self.icon_animation.start()
        else:  # Collapse the sidebar
            self.animation = QPropertyAnimation(self.side_menu, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(250)
            self.animation.setEndValue(0)  # Collapse sidebar
            self.animation.start()

            self.icon_animation = QPropertyAnimation(self.side_menu_icon, b"maximumWidth")
            self.icon_animation.setDuration(300)
            self.icon_animation.setStartValue(0)
            self.icon_animation.setEndValue(50)  # Show icon-only menu
            self.icon_animation.start()


    def button_icon_change(self, status):
            if status:  # Sidebar closed
                self.menu_btn.setIcon(QIcon("./icon/open.png"))
                self.animate_sidebar(False)  # Collapse sidebar
            else:  # Sidebar opened
                self.menu_btn.setIcon(QIcon("./icon/close.png"))
                self.animate_sidebar(True)  # Expand sidebar


    def init_list_widget(self):
        self.side_menu.clear()
        self.side_menu_icon.clear()

        for menu in self.menu_list:
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setSizeHint(QSize(40,40))
            self.side_menu_icon.addItem(item)
            self.side_menu_icon.setCurrentRow(0)

            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu.get("icon")))
            item_new.setText(menu.get("name"))
            self.side_menu.addItem(item_new)
            self.side_menu.setCurrentRow

    # def init_stackwidget(self):
    #     widget_list = self.main_content.findChildren(QWidget)
    #     for widget in widget_list:
    #         self.main_content.removeWidget(widget)

    #     for menu in self.menu_list:
    #         text = menu.get("name")
    #         layout = QGridLayout()
    #         label = QLabel(text=text)
    #         label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    #         font = QFont()
    #         font.setPixelSize(20)
    #         label.setFont(font)
    #         layout.addWidget(label)
    #         new_page = QWidget()
    #         new_page.setLayout(layout)
    #         self.main_content.addWidget(new_page)



    def load_users_table(self):
        rows = self.db_manager.fetch_users()
        self.ui.tableUsers.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for col_index, col_data in enumerate(row_data):
                self.ui.tableUsers.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def load_admins_table(self):
        rows = self.db_manager.fetch_admins()
        self.ui.tableAdmins.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for col_index, col_data in enumerate(row_data):
                self.ui.tableAdmins.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def load_logs_table(self):
        rows = self.db_manager.fetch_logs()
        self.ui.tableLogs.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for col_index, col_data in enumerate(row_data):
                self.ui.tableLogs.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def load_departments_table(self):
        rows = self.db_manager.fetch_departments()
        self.ui.tableDepartements.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for col_index, col_data in enumerate(row_data):
                self.ui.tableDepartements.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    
    def load_feedback_table(self):
        rows = self.db_manager.fetch_feedback()
        self.ui.tableFeddback.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for col_index, col_data in enumerate(row_data):
                if(col_index == 2):
                        if col_data == 1:
                             col_data = "True"
                        else:
                             col_data = "False"
                self.ui.tableFeddback.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def closeEvent(self, event):
        # Close the database connection when the window is closed
        self.db_manager.close_connection()
        super().closeEvent(event)

    # Users start

    def remove_selected_users(self):
        selected_rows = self.ui.tableUsers.selectionModel().selectedRows()  # Get all selected rows
        if not selected_rows:  # No rows selected
            QMessageBox.warning(self, "Selection Error", "Please select one or more rows first.")
            return

        # Confirm deletion
        confirmation = QMessageBox.question(
            self, 
            "Confirm Deletion", 
            f"Are you sure you want to delete {len(selected_rows)} user(s)?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmation == QMessageBox.StandardButton.No:
            return

        # Iterate through selected rows and delete users
        user_ids = []
        for row in selected_rows:
            row_index = row.row()
            user_id = self.ui.tableUsers.item(row_index, 0).text()  # Assuming ID is in column 0
            user_ids.append(user_id)

        # Call the database manager to delete users
        self.db_manager.delete_users(user_ids)  # Modify delete_users method in the DatabaseManager

        # Reload the table after deletion
        self.load_users_table()

    def open_user_crud(self, mode="add", user_data=None):
        """
        Open the UserCRUD window for adding or editing a user.
        :param mode: "add" for adding a new user, "edit" for editing an existing user
        :param user_data: Dictionary containing existing user data (for edit mode)
        """
        
        self.user_crud_window = UserCRUDWindow(self)
        self.user_crud_window.stat = "add"
        if mode == "edit" and user_data:
            self.user_crud_window.stat = "edit"
            self.user_crud_window.populate_form(user_data)
        
        
        self.user_crud_window.show()

    def edit_selected_user(self):
        selected_row = self.ui.tableUsers.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a user to edit.")
            return

        user_data = {
            "id_user" : self.ui.tableUsers.item(selected_row, 0).text(),
            "name": self.ui.tableUsers.item(selected_row, 1).text(),
            "photo_path": self.ui.tableUsers.item(selected_row, 2).text(),
            "dep": self.ui.tableUsers.item(selected_row, 3).text(),
            "role": self.ui.tableUsers.item(selected_row, 4).text(),
        }

        self.open_user_crud(mode="edit", user_data=user_data)
    
    # Users end

    # Departement start
    def remove_selected_deps(self):
        selected_rows = self.ui.tableDepartements.selectionModel().selectedRows()  # Get all selected rows
        if not selected_rows:  # No rows selected
            QMessageBox.warning(self, "Selection Error", "Please select one or more rows first.")
            return

        # Confirm deletion
        confirmation = QMessageBox.question(
            self, 
            "Confirm Deletion", 
            f"Are you sure you want to delete {len(selected_rows)} departement(s)?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmation == QMessageBox.StandardButton.No:
            return

        dep_ids = []
        for row in selected_rows:
            row_index = row.row()
            dep_id = self.ui.tableDepartements.item(row_index, 0).text()  # Assuming ID is in column 0
            dep_ids.append(dep_id)

        # Call the database manager to delete users
        self.db_manager.delete_department(dep_ids)  

        # Reload the table after deletion
        self.load_departments_table()

    def open_dep_crud(self, mode="add", dep_data=None):
        self.dep_crud_window = DepartementCRUDWindow(self)
        self.dep_crud_window.stat = "add"
        if mode == "edit" and dep_data:
            self.dep_crud_window.stat = "edit"
            self.dep_crud_window.populate_form(dep_data)
        
        self.dep_crud_window.show()

    def edit_selected_dep(self):
        selected_row = self.ui.tableDepartements.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a user to edit.")
            return

        dep_data = {
            "id_dep" : self.ui.tableDepartements.item(selected_row, 0).text(),
            "name": self.ui.tableDepartements.item(selected_row, 1).text(),
        }

        self.open_dep_crud(mode="edit", dep_data=dep_data)

    # Departement end

    # Admins Start
    def remove_selected_admins(self):
        selected_rows = self.ui.tableAdmins.selectionModel().selectedRows()  # Get all selected rows
        if not selected_rows:  # No rows selected
            QMessageBox.warning(self, "Selection Error", "Please select one or more rows first.")
            return

        # Confirm deletion
        confirmation = QMessageBox.question(
            self, 
            "Confirm Deletion", 
            f"Are you sure you want to delete {len(selected_rows)} Admin(s)?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmation == QMessageBox.StandardButton.No:
            return

        admin_ids = []
        for row in selected_rows:
            row_index = row.row()
            admin_id = self.ui.tableAdmins.item(row_index, 0).text()  # Assuming ID is in column 0
            admin_ids.append(admin_id)

        # Call the database manager to delete users
        self.db_manager.delete_admins(admin_ids)  

        # Reload the table after deletion
        self.load_admins_table()

    def open_admins_crud(self, mode="add", admin_data=None):
        self.admin_crud_window = AdminCRUDWindow(self)
        self.admin_crud_window.stat = "add"
        if mode == "edit" and admin_data:
            self.admin_crud_window.stat = "edit"
            self.admin_crud_window.populate_form(admin_data)
        
        self.admin_crud_window.show()

    def edit_selected_admin(self):
        selected_row = self.ui.tableAdmins.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a user to edit.")
            return

        admin_data = {
            "admin_id" : self.ui.tableAdmins.item(selected_row, 0).text(),
            "user": self.ui.tableAdmins.item(selected_row, 1).text(),
            "email": self.ui.tableAdmins.item(selected_row, 2).text(),
            "password": self.ui.tableAdmins.item(selected_row, 3).text(),
        }

        self.open_admins_crud(mode="edit", admin_data=admin_data)

# Admins end

# Research start

    def user_search(self):
        item = self.ui.cmbUsers.currentText()  # Get the selected search criterion (e.g., "Id", "Nom", etc.)
        search_value = self.ui.txtUser.text()  # Get the value to search for
        table = self.ui.tableUsers  # Assuming the table widget is named tableUsers

        # List of rows to delete
        rows_to_delete = []

        for row in range(table.rowCount()):
                if item == "Id":
                        if table.item(row, 0).text() != search_value:  # Assuming Id is in the first column (index 0)
                                rows_to_delete.append(row)  # Mark row for deletion
                elif item == "Nom":
                        if table.item(row, 1).text().lower() != search_value.lower():  # Assuming Name is in the second column (index 1)
                                rows_to_delete.append(row)  # Mark row for deletion
                elif item == "Departement":
                        if table.item(row, 3).text().lower() != search_value.lower():  # Assuming Departement is in the third column (index 2)
                                rows_to_delete.append(row)  # Mark row for deletion
                elif item == "Role":
                        if table.item(row, 4).text().lower() != search_value.lower():  # Assuming Role is in the fourth column (index 3)
                                rows_to_delete.append(row)  # Mark row for deletion

        # Now delete the marked rows
        for row in reversed(rows_to_delete):
                table.removeRow(row)


#     def logs_search(self):
#         # Get the selected start and end dates from the QDateEdit widgets
#         start_date = self.ui.dateEdit_1.date().toPyDate()  # Start date from QDateEdit
#         end_date = self.ui.dateEdit_2.date().toPyDate()  # End date from QDateEdit
#         table = self.ui.tableLogs  # Assuming the table widget is named tableUsers

#         # List of rows to delete
#         rows_to_delete = []

#         # Iterate over all rows and check if the timestamp is within the date range
#         for row in range(table.rowCount()):
#                 # Assuming Timestamp is in the fifth column (index 4) in format 'YYYY-MM-DD HH:MM:SS'
#                 timestamp_str = table.item(row, 2).text()  # Get the timestamp string from the table
#                 print(timestamp_str)

#                 # try:
#                 #         print(start_date,end_date)
#                 #         print(timestamp_str)
#                 #         row_timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")  # Adjust format if needed
#                 #         print(row_timestamp)
#                 #         print("#########╠")


#                 #         if not (start_date <= row_timestamp.date() <= end_date):  # Only compare the date part
#                 #                 rows_to_delete.append(row)

#                 # except ValueError:
#                 #         # If there's an issue parsing the timestamp, you can skip that row or log a message
#                 #         print(f"Invalid timestamp format in row {row}. Skipping this row.")
#                 # continue

#         # Now delete the marked rows
#         for row in reversed(rows_to_delete):
#                 table.removeRow(row)

    def feed_back_search(self):
        item = self.ui.cmbFeedback.currentIndex()  
        table = self.ui.tableFeddback  

        # List of rows to delete
        rows_to_delete = []

        for row in range(table.rowCount()):
                if item == 0:
                        if table.item(row, 2).text() != "True":  
                                rows_to_delete.append(row)  
                if item == 1:
                        if table.item(row, 2).text() != "False": 
                                rows_to_delete.append(row)

        # Now delete the marked rows
        for row in reversed(rows_to_delete):
                table.removeRow(row)



# Research end

    def load_settings(self):
        self.ui.conf.setSuffix(" %")
        row = self.db_manager.fetch_setttings()
        self.ui.conf.setValue(row[0][0])
        self.ui.txtEmailReceiver.setText(row[0][1])
        self.ui.txtEmailSender.setText(row[0][2])
        self.ui.txtPassword.setText(row[0][3])

    def update_settings(self):
        treshhold = self.ui.conf.value()
        email_sender = self.ui.txtEmailSender.text().strip()
        email_receiver = self.ui.txtEmailReceiver.text().strip()
        password = self.ui.txtPassword.text().strip()
        
        if not treshhold or not email_sender or not email_receiver or not password :
                QMessageBox.warning(self, "Input Error", "All fields are required!")
                return
        self.db_manager.update_settings(treshhold,email_sender,email_receiver,password)
        QMessageBox.information(self, "Success", "Settings updated successfully")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss") as f:
        style_str = f.read()

    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

