# Form implementation generated from reading ui file '.\uis\UserCRUD.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from db_operations import DatabaseManager


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 340)
        MainWindow.setMinimumSize(QtCore.QSize(420, 340))
        MainWindow.setMaximumSize(QtCore.QSize(420, 340))
        MainWindow.setStyleSheet("background-color: rgb(254, 254, 254);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_2 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(120, 110, 179, 22))
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(parent=self.splitter_2)
        self.label_2.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.txtphotoPath = QtWidgets.QLineEdit(parent=self.splitter_2)
        self.txtphotoPath.setObjectName("txtphotoPath")
        self.splitter_3 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(120, 160, 179, 22))
        self.splitter_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(parent=self.splitter_3)
        self.label_3.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.cmbDep = QtWidgets.QComboBox(parent=self.splitter_3)
        self.cmbDep.setObjectName("cmbDep")
        self.splitter_4 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_4.setGeometry(QtCore.QRect(120, 200, 179, 22))
        self.splitter_4.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_4 = QtWidgets.QLabel(parent=self.splitter_4)
        self.label_4.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.cmbRole = QtWidgets.QComboBox(parent=self.splitter_4)
        self.cmbRole.setObjectName("cmbRole")
        self.cmbRole.addItem("")
        self.cmbRole.addItem("")
        self.btnConfUser = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnConfUser.setGeometry(QtCore.QRect(160, 250, 93, 28))
        self.btnConfUser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.btnConfUser.setObjectName("btnConfUser")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(120, 60, 179, 22))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(parent=self.splitter)
        self.label.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.txtName = QtWidgets.QLineEdit(parent=self.splitter)
        self.txtName.setObjectName("txtName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Photo path :"))
        self.label_3.setText(_translate("MainWindow", "Departement :"))
        self.label_4.setText(_translate("MainWindow", "Role :"))
        self.cmbRole.setItemText(0, _translate("MainWindow", "Admin"))
        self.cmbRole.setItemText(1, _translate("MainWindow", "Employee"))
        self.btnConfUser.setText(_translate("MainWindow", "Confirmer"))
        self.label.setText(_translate("MainWindow", "Name :"))


from PyQt6.QtWidgets import QMainWindow, QMessageBox

class UserCRUDWindow(QMainWindow):
    def __init__(self, parent=None):
        super(UserCRUDWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize database manager
        self.db_manager = DatabaseManager()

        # Connect the "Confirmer" button to a method
        self.ui.btnConfUser.clicked.connect(self.confirm_Dep)
        
        self.stat = ""
        self.idUser = 0

        self.load_departments()

    def confirm_Dep(self):

        id_user = self.idUser
        name = self.ui.txtName.text().strip()
        photo_path = self.ui.txtphotoPath.text().strip()
        dep_id, dep_name = self.get_selected_department()
        role = self.ui.cmbRole.currentText()
        if not name or not photo_path or not dep_id or not role:
                QMessageBox.warning(self, "Input Error", "All fields are required!")
                return
        if self.stat == "add":
            self.db_manager.add_user(name,photo_path,dep_id,role)
            QMessageBox.information(self, "Success", f"User '{name}' has been Added successfully!")
        elif self.stat == "edit":
            self.db_manager.update_user(id_user,name,photo_path,dep_id,role)
            QMessageBox.information(self, "Success", f"User '{name}' has been Updated successfully!")
        
        self.close()

    def populate_form(self, user_data):
        """
        Populate the form fields with data for editing an existing user.
        :param user_data: Dictionary containing user data
        """
        self.idUser = int(user_data["id_user"])
        self.ui.txtName.setText(user_data.get("name", ""))
        self.ui.txtphotoPath.setText(user_data.get("photo_path", ""))
        self.ui.cmbDep.setCurrentText(user_data.get("dep", ""))
        self.ui.cmbRole.setCurrentText(user_data.get("role", ""))

    def load_departments(self):
        departments = self.db_manager.get_departments_from_db()  # Example: [(id1, name1), (id2, name2), ...]
        self.ui.cmbDep.clear()

        for dept_id, dept_name in departments:
            self.ui.cmbDep.addItem(dept_name, dept_id)  # Add the name as visible text and ID as associated data

    def get_selected_department(self):
        # Get the index of the currently selected item
        index = self.ui.cmbDep.currentIndex()
        if index == -1:  # No selection
            return None, None

        # Get the department name (displayed text)
        dep_name = self.ui.cmbDep.currentText()
        
        # Get the department ID (stored as user data)
        dep_id = self.ui.cmbDep.itemData(index)

        return dep_id, dep_name




