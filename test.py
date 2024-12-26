from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Interface")

        # Create the central widget
        central_widget = QWidget(self)
        central_layout = QHBoxLayout(central_widget)

        # Sidebar (fixed on the left)
        self.sidebar = QFrame(self)
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFixedWidth(200)  # Set the sidebar to a fixed width
        self.sidebar_layout = QVBoxLayout(self.sidebar)

        # Add buttons to sidebar
        self.btnDashboard = QPushButton("Dashboard", self)
        self.btnManageEmployees = QPushButton("Manage Employees", self)
        self.btnLogs = QPushButton("Logs", self)
        self.btnDepartments = QPushButton("Departments", self)
        self.btnAdmins = QPushButton("Admins", self)
        self.btnSettings = QPushButton("Settings", self)

        self.sidebar_layout.addWidget(self.btnDashboard)
        self.sidebar_layout.addWidget(self.btnManageEmployees)
        self.sidebar_layout.addWidget(self.btnLogs)
        self.sidebar_layout.addWidget(self.btnDepartments)
        self.sidebar_layout.addWidget(self.btnAdmins)
        self.sidebar_layout.addWidget(self.btnSettings)

        # Create the main content area using QStackedWidget
        self.main_content = QStackedWidget(self)

        # Create pages for main content
        self.dashboard_page = QWidget()
        self.manage_employees_page = QWidget()
        self.logs_page = QWidget()

        # Add pages to the QStackedWidget
        self.main_content.addWidget(self.dashboard_page)
        self.main_content.addWidget(self.manage_employees_page)
        self.main_content.addWidget(self.logs_page)

        # Set initial page
        self.main_content.setCurrentWidget(self.dashboard_page)

        # Create header
        self.header = QFrame(self)
        self.header_layout = QHBoxLayout(self.header)
        self.admin_name_label = QLabel("Admin: John Doe", self)
        self.timestamp_label = QLabel("Timestamp: 12/12/2024", self)
        self.header_layout.addWidget(self.admin_name_label)
        self.header_layout.addWidget(self.timestamp_label)

        # Add sidebar, header, and main content to the layout
        central_layout.addWidget(self.sidebar)
        central_layout.addWidget(self.main_content)

        # Set central widget
        self.setCentralWidget(central_widget)

        # Connect buttons to switch content
        self.btnDashboard.clicked.connect(self.show_dashboard)
        self.btnManageEmployees.clicked.connect(self.show_manage_employees)
        self.btnLogs.clicked.connect(self.show_logs)

    def show_dashboard(self):
        self.main_content.setCurrentWidget(self.dashboard_page)

    def show_manage_employees(self):
        self.main_content.setCurrentWidget(self.manage_employees_page)

    def show_logs(self):
        self.main_content.setCurrentWidget(self.logs_page)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
