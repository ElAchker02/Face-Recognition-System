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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1581, 844)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)

        self.listWidget_icon = QListWidget(self.centralwidget)
        self.listWidget_icon.setObjectName(u"listWidget_icon")
        self.listWidget_icon.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.listWidget_icon, 1, 0, 1, 1)

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

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.admin = QLabel(self.frame_2)
        self.admin.setObjectName(u"admin")
        self.admin.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_2.addWidget(self.admin)

        self.timestamps = QLabel(self.frame_2)
        self.timestamps.setObjectName(u"timestamps")
        self.timestamps.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.timestamps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.timestamps)


        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.widget = QWidget(self.dashboard_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 60, 1251, 521))
        self.gridLayout_9 = QGridLayout(self.widget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.nbUsers = QLabel(self.groupBox)
        self.nbUsers.setObjectName(u"nbUsers")
        self.nbUsers.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.nbUsers, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.entriesToday = QLabel(self.groupBox_3)
        self.entriesToday.setObjectName(u"entriesToday")
        self.entriesToday.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.entriesToday, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.nbUnrecognizedToday = QLabel(self.groupBox_2)
        self.nbUnrecognizedToday.setObjectName(u"nbUnrecognizedToday")
        self.nbUnrecognizedToday.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.nbUnrecognizedToday, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.nbRecognizedPersons = QLabel(self.groupBox_4)
        self.nbRecognizedPersons.setObjectName(u"nbRecognizedPersons")
        self.nbRecognizedPersons.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.nbRecognizedPersons, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_4, 0, 3, 1, 1)

        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.wrongPrediction = QLabel(self.groupBox_5)
        self.wrongPrediction.setObjectName(u"wrongPrediction")
        self.wrongPrediction.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.wrongPrediction, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_5, 1, 0, 1, 2)

        self.groupBox_6 = QGroupBox(self.widget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.truePredictions = QLabel(self.groupBox_6)
        self.truePredictions.setObjectName(u"truePredictions")
        self.truePredictions.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.truePredictions, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_6, 1, 2, 1, 1)

        self.groupBox_7 = QGroupBox(self.widget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.entrieslast7 = QLabel(self.groupBox_7)
        self.entrieslast7.setObjectName(u"entrieslast7")
        self.entrieslast7.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.entrieslast7, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_7, 1, 3, 1, 1)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.Users_page = QWidget()
        self.Users_page.setObjectName(u"Users_page")
        self.tableUsers = QTableWidget(self.Users_page)
        if (self.tableUsers.columnCount() < 5):
            self.tableUsers.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableUsers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableUsers.setObjectName(u"tableUsers")
        self.tableUsers.setGeometry(QRect(10, 80, 1271, 571))
        self.tableUsers.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableUsers.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.frame_6 = QFrame(self.Users_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 1301, 88))
        self.frame_6.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 30, 42, 21))
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(147, 30, 83, 21))
        self.txtUser = QLineEdit(self.frame_6)
        self.txtUser.setObjectName(u"txtUser")
        self.txtUser.setGeometry(QRect(350, 30, 171, 27))
        self.cmbUsers = QComboBox(self.frame_6)
        self.cmbUsers.addItem("")
        self.cmbUsers.addItem("")
        self.cmbUsers.addItem("")
        self.cmbUsers.addItem("")
        self.cmbUsers.setObjectName(u"cmbUsers")
        self.cmbUsers.setGeometry(QRect(252, 30, 87, 27))
        self.btnAddUser = QPushButton(self.frame_6)
        self.btnAddUser.setObjectName(u"btnAddUser")
        self.btnAddUser.setGeometry(QRect(593, 30, 93, 30))
        self.btnAddUser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        icon = QIcon()
        icon.addFile(u"../icon/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddUser.setIcon(icon)
        self.btnRefreshUser = QPushButton(self.frame_6)
        self.btnRefreshUser.setObjectName(u"btnRefreshUser")
        self.btnRefreshUser.setGeometry(QRect(10, 30, 41, 30))
        self.btnRefreshUser.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        icon1 = QIcon()
        icon1.addFile(u"../icon/ref.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRefreshUser.setIcon(icon1)
        self.btnExportUser = QPushButton(self.frame_6)
        self.btnExportUser.setObjectName(u"btnExportUser")
        self.btnExportUser.setGeometry(QRect(1180, 30, 93, 30))
        self.btnExportUser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        icon2 = QIcon()
        icon2.addFile(u"../icon/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportUser.setIcon(icon2)
        self.btnSearchUsers = QPushButton(self.frame_6)
        self.btnSearchUsers.setObjectName(u"btnSearchUsers")
        self.btnSearchUsers.setGeometry(QRect(530, 30, 41, 30))
        self.btnSearchUsers.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        icon3 = QIcon()
        icon3.addFile(u"../icon/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSearchUsers.setIcon(icon3)
        self.btnUpdateUser = QPushButton(self.frame_6)
        self.btnUpdateUser.setObjectName(u"btnUpdateUser")
        self.btnUpdateUser.setGeometry(QRect(720, 30, 93, 30))
        self.btnUpdateUser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        icon4 = QIcon()
        icon4.addFile(u"../icon/updae.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUpdateUser.setIcon(icon4)
        self.btnRmoveUser = QPushButton(self.frame_6)
        self.btnRmoveUser.setObjectName(u"btnRmoveUser")
        self.btnRmoveUser.setGeometry(QRect(850, 30, 93, 30))
        self.btnRmoveUser.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        icon5 = QIcon()
        icon5.addFile(u"../icon/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRmoveUser.setIcon(icon5)
        self.stackedWidget.addWidget(self.Users_page)
        self.logs_page = QWidget()
        self.logs_page.setObjectName(u"logs_page")
        self.frame_3 = QFrame(self.logs_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 1281, 88))
        self.frame_3.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 30, 42, 21))
        self.bntRefreshLogs = QPushButton(self.frame_3)
        self.bntRefreshLogs.setObjectName(u"bntRefreshLogs")
        self.bntRefreshLogs.setGeometry(QRect(10, 30, 41, 30))
        self.bntRefreshLogs.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.bntRefreshLogs.setIcon(icon1)
        self.btnExportLogs = QPushButton(self.frame_3)
        self.btnExportLogs.setObjectName(u"btnExportLogs")
        self.btnExportLogs.setGeometry(QRect(1180, 30, 93, 30))
        self.btnExportLogs.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExportLogs.setIcon(icon2)
        self.dateEdit_1 = QDateEdit(self.frame_3)
        self.dateEdit_1.setObjectName(u"dateEdit_1")
        self.dateEdit_1.setGeometry(QRect(230, 30, 110, 22))
        self.btnSearchLogs = QPushButton(self.frame_3)
        self.btnSearchLogs.setObjectName(u"btnSearchLogs")
        self.btnSearchLogs.setGeometry(QRect(580, 30, 41, 30))
        self.btnSearchLogs.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnSearchLogs.setIcon(icon3)
        self.dateEdit_2 = QDateEdit(self.frame_3)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(390, 30, 110, 22))
        self.tableLogs = QTableWidget(self.logs_page)
        if (self.tableLogs.columnCount() < 4):
            self.tableLogs.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.tableLogs.setObjectName(u"tableLogs")
        self.tableLogs.setGeometry(QRect(0, 90, 1281, 541))
        self.tableLogs.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableLogs.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableLogs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stackedWidget.addWidget(self.logs_page)
        self.departements_page = QWidget()
        self.departements_page.setObjectName(u"departements_page")
        self.frame_4 = QFrame(self.departements_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 1291, 61))
        self.frame_4.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btnRefreshDep = QPushButton(self.frame_4)
        self.btnRefreshDep.setObjectName(u"btnRefreshDep")
        self.btnRefreshDep.setGeometry(QRect(12, 12, 33, 29))
        self.btnRefreshDep.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btnRefreshDep.setIcon(icon1)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 10, 250, 30))
        self.tableDepartements = QTableWidget(self.departements_page)
        if (self.tableDepartements.columnCount() < 2):
            self.tableDepartements.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableDepartements.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableDepartements.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        self.tableDepartements.setObjectName(u"tableDepartements")
        self.tableDepartements.setGeometry(QRect(0, 90, 1281, 541))
        self.tableDepartements.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableDepartements.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableDepartements.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btnUpdateDep = QPushButton(self.departements_page)
        self.btnUpdateDep.setObjectName(u"btnUpdateDep")
        self.btnUpdateDep.setGeometry(QRect(440, 10, 93, 29))
        self.btnUpdateDep.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnUpdateDep.setIcon(icon4)
        self.btnRemoveDep = QPushButton(self.departements_page)
        self.btnRemoveDep.setObjectName(u"btnRemoveDep")
        self.btnRemoveDep.setGeometry(QRect(564, 10, 93, 29))
        self.btnRemoveDep.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btnRemoveDep.setIcon(icon5)
        self.btnAddDepartements = QPushButton(self.departements_page)
        self.btnAddDepartements.setObjectName(u"btnAddDepartements")
        self.btnAddDepartements.setGeometry(QRect(689, 10, 93, 29))
        self.btnAddDepartements.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnAddDepartements.setIcon(icon)
        self.btnExportDepartements = QPushButton(self.departements_page)
        self.btnExportDepartements.setObjectName(u"btnExportDepartements")
        self.btnExportDepartements.setGeometry(QRect(813, 10, 93, 29))
        self.btnExportDepartements.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExportDepartements.setIcon(icon2)
        self.stackedWidget.addWidget(self.departements_page)
        self.admins_page = QWidget()
        self.admins_page.setObjectName(u"admins_page")
        self.frame_5 = QFrame(self.admins_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 1281, 88))
        self.frame_5.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 30, 71, 21))
        self.btnRefeshAdmins = QPushButton(self.frame_5)
        self.btnRefeshAdmins.setObjectName(u"btnRefeshAdmins")
        self.btnRefeshAdmins.setGeometry(QRect(0, 30, 33, 29))
        self.btnRefeshAdmins.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btnRefeshAdmins.setIcon(icon1)
        self.layoutWidget = QWidget(self.frame_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(470, 30, 395, 32))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnUpdateAdmin = QPushButton(self.layoutWidget)
        self.btnUpdateAdmin.setObjectName(u"btnUpdateAdmin")
        self.btnUpdateAdmin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnUpdateAdmin.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.btnUpdateAdmin)

        self.btnRemoveAdmin = QPushButton(self.layoutWidget)
        self.btnRemoveAdmin.setObjectName(u"btnRemoveAdmin")
        self.btnRemoveAdmin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btnRemoveAdmin.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.btnRemoveAdmin)

        self.btnAddAdmins = QPushButton(self.layoutWidget)
        self.btnAddAdmins.setObjectName(u"btnAddAdmins")
        self.btnAddAdmins.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnAddAdmins.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btnAddAdmins)

        self.btnExportAdmins = QPushButton(self.layoutWidget)
        self.btnExportAdmins.setObjectName(u"btnExportAdmins")
        self.btnExportAdmins.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExportAdmins.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.btnExportAdmins)

        self.tableAdmins = QTableWidget(self.admins_page)
        if (self.tableAdmins.columnCount() < 4):
            self.tableAdmins.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.tableAdmins.setObjectName(u"tableAdmins")
        self.tableAdmins.setGeometry(QRect(0, 90, 1281, 621))
        self.tableAdmins.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableAdmins.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableAdmins.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stackedWidget.addWidget(self.admins_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.tableFeddback = QTableWidget(self.settings_page)
        if (self.tableFeddback.columnCount() < 4):
            self.tableFeddback.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableFeddback.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableFeddback.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableFeddback.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableFeddback.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.tableFeddback.setObjectName(u"tableFeddback")
        self.tableFeddback.setGeometry(QRect(10, 100, 1281, 541))
        self.tableFeddback.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableFeddback.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableFeddback.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableFeddback.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btnRefreshFeedback = QPushButton(self.settings_page)
        self.btnRefreshFeedback.setObjectName(u"btnRefreshFeedback")
        self.btnRefreshFeedback.setGeometry(QRect(20, 40, 41, 30))
        self.btnRefreshFeedback.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.btnRefreshFeedback.setIcon(icon1)
        self.btnSearchFeedback = QPushButton(self.settings_page)
        self.btnSearchFeedback.setObjectName(u"btnSearchFeedback")
        self.btnSearchFeedback.setGeometry(QRect(510, 40, 41, 30))
        self.btnSearchFeedback.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnSearchFeedback.setIcon(icon3)
        self.btnExporFeedback = QPushButton(self.settings_page)
        self.btnExporFeedback.setObjectName(u"btnExporFeedback")
        self.btnExporFeedback.setGeometry(QRect(1190, 40, 93, 30))
        self.btnExporFeedback.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExporFeedback.setIcon(icon2)
        self.label_4 = QLabel(self.settings_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 40, 71, 21))
        self.label_8 = QLabel(self.settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 40, 121, 16))
        self.cmbFeedback = QComboBox(self.settings_page)
        self.cmbFeedback.addItem("")
        self.cmbFeedback.addItem("")
        self.cmbFeedback.setObjectName(u"cmbFeedback")
        self.cmbFeedback.setGeometry(QRect(380, 40, 73, 22))
        self.stackedWidget.addWidget(self.settings_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 0, 231, 101))
        self.label.setStyleSheet(u"font: 75 30pt \"MS Shell Dlg 2\";")
        self.layoutWidget1 = QWidget(self.page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 120, 471, 251))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.txtEmailSender = QLineEdit(self.layoutWidget1)
        self.txtEmailSender.setObjectName(u"txtEmailSender")

        self.gridLayout_2.addWidget(self.txtEmailSender, 1, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.txtPassword = QLineEdit(self.layoutWidget1)
        self.txtPassword.setObjectName(u"txtPassword")

        self.gridLayout_2.addWidget(self.txtPassword, 3, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.txtEmailReceiver = QLineEdit(self.layoutWidget1)
        self.txtEmailReceiver.setObjectName(u"txtEmailReceiver")

        self.gridLayout_2.addWidget(self.txtEmailReceiver, 2, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)

        self.conf = QSpinBox(self.layoutWidget1)
        self.conf.setObjectName(u"conf")

        self.gridLayout_2.addWidget(self.conf, 0, 1, 1, 1)

        self.btnUpdateSettings = QPushButton(self.layoutWidget1)
        self.btnUpdateSettings.setObjectName(u"btnUpdateSettings")
        self.btnUpdateSettings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnUpdateSettings.setIcon(icon4)

        self.gridLayout_2.addWidget(self.btnUpdateSettings, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1581, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.title2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.admin.setText(QCoreApplication.translate("MainWindow", u"Amine", None))
        self.timestamps.setText(QCoreApplication.translate("MainWindow", u"timestamps", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Total Users", None))
        self.nbUsers.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Entries Today", None))
        self.entriesToday.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Unrecognized Persons Today", None))
        self.nbUnrecognizedToday.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Recognized Persons Today", None))
        self.nbRecognizedPersons.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Number of wrong predictions", None))
        self.wrongPrediction.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Number of true predictions", None))
        self.truePredictions.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Entries Last 7 days", None))
        self.entrieslast7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem = self.tableUsers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableUsers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableUsers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Photo", None));
        ___qtablewidgetitem3 = self.tableUsers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Departement", None));
        ___qtablewidgetitem4 = self.tableUsers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Search by :", None))
        self.cmbUsers.setItemText(0, QCoreApplication.translate("MainWindow", u"Id", None))
        self.cmbUsers.setItemText(1, QCoreApplication.translate("MainWindow", u"Name", None))
        self.cmbUsers.setItemText(2, QCoreApplication.translate("MainWindow", u"Departement", None))
        self.cmbUsers.setItemText(3, QCoreApplication.translate("MainWindow", u"Role", None))

        self.btnAddUser.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btnRefreshUser.setText("")
        self.btnExportUser.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.btnSearchUsers.setText("")
        self.btnUpdateUser.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btnRmoveUser.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.bntRefreshLogs.setText("")
        self.btnExportLogs.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.btnSearchLogs.setText("")
        ___qtablewidgetitem5 = self.tableLogs.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Id log", None));
        ___qtablewidgetitem6 = self.tableLogs.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"User", None));
        ___qtablewidgetitem7 = self.tableLogs.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Timstamp", None));
        ___qtablewidgetitem8 = self.tableLogs.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Emotion", None));
        self.btnRefreshDep.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Departements", None))
        ___qtablewidgetitem9 = self.tableDepartements.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Id Departement", None));
        ___qtablewidgetitem10 = self.tableDepartements.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Departement Name", None));
        self.btnUpdateDep.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btnRemoveDep.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btnAddDepartements.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btnExportDepartements.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Admins", None))
        self.btnRefeshAdmins.setText("")
        self.btnUpdateAdmin.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btnRemoveAdmin.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btnAddAdmins.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btnExportAdmins.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        ___qtablewidgetitem11 = self.tableAdmins.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Id Admin", None));
        ___qtablewidgetitem12 = self.tableAdmins.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"User", None));
        ___qtablewidgetitem13 = self.tableAdmins.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem14 = self.tableAdmins.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem15 = self.tableFeddback.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"id Feedback", None));
        ___qtablewidgetitem16 = self.tableFeddback.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"id Log", None));
        ___qtablewidgetitem17 = self.tableFeddback.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Prediction state", None));
        ___qtablewidgetitem18 = self.tableFeddback.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Reel User", None));
        self.btnRefreshFeedback.setText("")
        self.btnSearchFeedback.setText("")
        self.btnExporFeedback.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Feed back", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Prediction State :", None))
        self.cmbFeedback.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.cmbFeedback.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Confidence Tresh hold :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Email Sender :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Email Receiver :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.btnUpdateSettings.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

