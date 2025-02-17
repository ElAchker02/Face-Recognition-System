# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QCursor
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QMessageBox
from PySide6.QtWidgets import QLabel, QPushButton
import sqlite3
from main import MainWindow

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 620)
        Dialog.setMinimumSize(QSize(480, 620))
        Dialog.setMaximumSize(QSize(480, 620))

        # icon = QIcon('images/facial-recognition.png')
        # Dialog.setWindowIcon(icon)

        icon = QIcon()
        icon.addFile("images/iconLogin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(247, 247, 247);")

        self.label = QLabel(Dialog)
        self.label.setGeometry(170, 50, 151, 131)
        self.label.setPixmap(QPixmap("images/user.png"))

        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(80, 240, 101, 21)
        self.label_2.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        self.label_2.setText("Email:")

        self.email = QLineEdit(Dialog)
        self.email.setGeometry(80, 270, 310, 30)

        self.password = QLineEdit(Dialog)
        self.password.setGeometry(80, 350, 310, 30)
        self.password.setEchoMode(QLineEdit.Password)

        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(80, 320, 101, 21)
        self.label_3.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        self.label_3.setText("Password:")

        self.btnLogin = QPushButton(Dialog)
        self.btnLogin.setGeometry(170, 440, 161, 41)
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet("font: 10pt 'MS Shell Dlg 2';\n"
                                    "background-color: rgb(40, 207, 254);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 75 8pt 'MS Shell Dlg 2';\n"
                                    "font: 75 10pt 'MS Shell Dlg 2';\n"
                                    "QPushButton:hover {\n"
                                    "   background-color: rgb(40, 207, 254);\n"
                                    "   color: rgb(255, 255, 255);\n"
                                    "}")

        self.btnLogin.setText("Login")

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.center_on_screen()

        # Connect button action
        self.ui.btnLogin.clicked.connect(self.login_action)
        self.ui.password.returnPressed.connect(self.login_action)

    def center_on_screen(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        dialog_geometry = self.geometry()
        x = (screen_geometry.width() - dialog_geometry.width()) // 2
        y = (screen_geometry.height() - dialog_geometry.height()) // 2
        self.move(x, y)

    def login_action(self):
        email = self.ui.email.text().strip()
        password = self.ui.password.text().strip()

        # Validate inputs
        if not email or not password:
            QMessageBox.warning(self, "Error", "Please enter both email and password!")
            return

        # Attempt to login
        if self.authenticate_user(email, password):
            self.open_main_interface(email)
        else:
            QMessageBox.warning(self, "Error", "Invalid email or password!")

    def authenticate_user(self, email, password):
        # Connect to SQLite database
        try: 
            connection = sqlite3.connect("db/face_recognition.db")
            cursor = connection.cursor()

            # Query the Admins table
            cursor.execute("SELECT * FROM Admins WHERE email = ? AND password = ?", (email, password))
            result = cursor.fetchone()

            # Close the connection
            connection.close()

            # Return True if user is found
            return result is not None
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            return False

    def open_main_interface(self, user_name):
        # Hide the login window
        self.hide()
        
        # Create and show the main interface
        self.main_window = MainWindow(user_name)
        self.main_window.show()

if __name__ == "__main__":
    app = QApplication([])
    dialog = LoginDialog()
    dialog.show()
    app.exec()
