from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QLineEdit, QComboBox
from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialisation des widgets
        self.setWindowTitle("Recherche dans le tableau")
        self.resize(800, 600)

        self.table_view = QTableView(self)
        self.search_bar = QLineEdit(self)
        self.combo_box = QComboBox(self)

        # Configuration des colonnes à rechercher
        self.combo_box.addItems(["Nom", "Prénom", "Email"])  # Les colonnes que tu veux rechercher

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.search_bar)
        layout.addWidget(self.table_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Configuration du modèle de données
        self.model = QStandardItemModel(0, 3, self)  # 3 colonnes
        self.model.setHorizontalHeaderLabels(["Nom", "Prénom", "Email"])
        self.populate_table()

        # Modèle de filtre
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)
        # self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)  # Insensible à la casse
        # self.proxy_model.setFilterKeyColumn(0)  # Par défaut, colonne 0 (Nom)

        # Lier le modèle au tableau
        self.table_view.setModel(self.proxy_model)

        # Connexions
        self.search_bar.textChanged.connect(self.update_filter)
        self.combo_box.currentIndexChanged.connect(self.update_filter_column)

    def populate_table(self):
        """Ajouter des données au tableau."""
        data = [
            ["Amine", "El Amrani", "amine.elamrani@example.com"],
            ["Yassine", "Benzakour", "yassine.benzakour@example.com"],
            ["Sarah", "Belkadi", "sarah.belkadi@example.com"],
            ["Hajar", "El Idrissi", "hajar.elidrissi@example.com"]
        ]
        for row in data:
            items = [QStandardItem(field) for field in row]
            self.model.appendRow(items)

    def update_filter(self, text):
        """Met à jour le filtre en fonction du texte entré."""
        self.proxy_model.setFilterFixedString(text)

    def update_filter_column(self, index):
        """Met à jour la colonne à filtrer en fonction de la sélection dans la ComboBox."""
        self.proxy_model.setFilterKeyColumn(index)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
