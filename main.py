from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from ui import Ui_Dialog
from dbmanager import DBManager, DBViewer


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_manager = DBManager()
        self.db_viewer = DBViewer()

        # Create tables if they don't exist
        self.db_manager.create_table()

        # Connect search functionality to input fields
        self.NAMEINPUT.textChanged.connect(self.search_records)
        self.REGISTRATIONINPUT.textChanged.connect(self.search_records)
        self.MAKEINPUT.textChanged.connect(self.search_records)
        self.MODELINPUT.textChanged.connect(self.search_records)

        # Connect category buttons
        self.STUDENTCARS.clicked.connect(lambda: self.filter_by_role("STUDENT"))
        self.VISITORCARS.clicked.connect(lambda: self.filter_by_role("VISITOR"))
        self.STAFFCARS.clicked.connect(lambda: self.filter_by_role("STAFF"))

        # Initialize table
        self.setup_table()
        self.load_all_records()

    def setup_table(self):
        headers = [
            "ID",
            "First Name",
            "Last Name",
            "Role",
            "Make",
            "Model",
            "Registration",
            "Date Issued",
            "Date Expiry",
        ]
        self.DETAILTABLE.setColumnCount(len(headers))
        self.DETAILTABLE.setHorizontalHeaderLabels(headers)
        self.DETAILTABLE.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.DETAILTABLE.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.DETAILTABLE.setSortingEnabled(True)
        self.DETAILTABLE.horizontalHeader().setStretchLastSection(True)
        self.DETAILTABLE.verticalHeader().setVisible(False)
        
        # Set column widths
        self.DETAILTABLE.setColumnWidth(0, 50)  # ID
        self.DETAILTABLE.setColumnWidth(1, 100)  # First Name
        self.DETAILTABLE.setColumnWidth(2, 100)  # Last Name
        self.DETAILTABLE.setColumnWidth(3, 80)   # Role
        self.DETAILTABLE.setColumnWidth(4, 100)  # Make
        self.DETAILTABLE.setColumnWidth(5, 100)  # Model
        self.DETAILTABLE.setColumnWidth(6, 100)  # Registration

    def search_records(self):
        name_parts = self.NAMEINPUT.text().strip().split()
        fname = name_parts[0] if name_parts else None
        lname = name_parts[1] if len(name_parts) > 1 else None

        results = self.db_viewer.search(
            fname=fname,
            lname=lname,
            make=self.MAKEINPUT.text() or None,
            model=self.MODELINPUT.text() or None,
            reg=self.REGISTRATIONINPUT.text() or None,
        )
        self.update_table(results)

    def filter_by_role(self, role):
        results = self.db_viewer.search(role=role)
        self.update_table(results)

    def update_table(self, records):
        try:
            self.DETAILTABLE.setRowCount(len(records))
            for row, record in enumerate(records):
                for col, value in enumerate(record):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)  # Make readonly
                    self.DETAILTABLE.setItem(row, col, item)
            self.DETAILTABLE.resizeColumnsToContents()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to update table: {str(e)}")

    def load_all_records(self):
        results = self.db_viewer.search()
        self.update_table(results)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
