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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
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
        self.timestamps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.timestamps)


        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)

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
        self.tableUsers.setGeometry(QRect(10, 80, 1271, 621))
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
        self.dateEdit = QDateEdit(self.frame_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(230, 30, 110, 22))
        self.btnSearchLogs = QPushButton(self.frame_3)
        self.btnSearchLogs.setObjectName(u"btnSearchLogs")
        self.btnSearchLogs.setGeometry(QRect(370, 30, 41, 30))
        self.btnSearchLogs.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnSearchLogs.setIcon(icon3)
        self.tableLogs = QTableWidget(self.logs_page)
        if (self.tableLogs.columnCount() < 3):
            self.tableLogs.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(2, __qtablewidgetitem7)
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
        self.frame_4.setGeometry(QRect(0, 0, 530, 54))
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
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableDepartements.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableDepartements.setHorizontalHeaderItem(1, __qtablewidgetitem9)
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
        self.widget = QWidget(self.frame_5)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(470, 30, 395, 32))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnUpdateAdmin = QPushButton(self.widget)
        self.btnUpdateAdmin.setObjectName(u"btnUpdateAdmin")
        self.btnUpdateAdmin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btnUpdateAdmin.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.btnUpdateAdmin)

        self.btnRemoveAdmin = QPushButton(self.widget)
        self.btnRemoveAdmin.setObjectName(u"btnRemoveAdmin")
        self.btnRemoveAdmin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btnRemoveAdmin.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.btnRemoveAdmin)

        self.btnAddAdmins = QPushButton(self.widget)
        self.btnAddAdmins.setObjectName(u"btnAddAdmins")
        self.btnAddAdmins.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnAddAdmins.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btnAddAdmins)

        self.btnExportAdmins = QPushButton(self.widget)
        self.btnExportAdmins.setObjectName(u"btnExportAdmins")
        self.btnExportAdmins.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.btnExportAdmins.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.btnExportAdmins)

        self.tableAdmins = QTableWidget(self.admins_page)
        if (self.tableAdmins.columnCount() < 4):
            self.tableAdmins.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableAdmins.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.tableAdmins.setObjectName(u"tableAdmins")
        self.tableAdmins.setGeometry(QRect(0, 90, 1281, 621))
        self.tableAdmins.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableAdmins.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableAdmins.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stackedWidget.addWidget(self.admins_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_4 = QLabel(self.settings_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 280, 55, 16))
        self.stackedWidget.addWidget(self.settings_page)

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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.admin.setText(QCoreApplication.translate("MainWindow", u"Amine", None))
        self.timestamps.setText(QCoreApplication.translate("MainWindow", u"timestamps", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.title2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        ___qtablewidgetitem = self.tableUsers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableUsers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem2 = self.tableUsers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"photo", None));
        ___qtablewidgetitem3 = self.tableUsers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"departement", None));
        ___qtablewidgetitem4 = self.tableUsers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"role", None));
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
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Timstamp", None));
        ___qtablewidgetitem7 = self.tableLogs.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Emotion", None));
        self.btnRefreshDep.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Departements", None))
        ___qtablewidgetitem8 = self.tableDepartements.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Id Departement", None));
        ___qtablewidgetitem9 = self.tableDepartements.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Departement Name", None));
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
        ___qtablewidgetitem10 = self.tableAdmins.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Id Admin", None));
        ___qtablewidgetitem11 = self.tableAdmins.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"User", None));
        ___qtablewidgetitem12 = self.tableAdmins.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem13 = self.tableAdmins.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"settings", None))
    # retranslateUi

