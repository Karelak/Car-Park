from ui import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sys
import sqlite3


class CarParkApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connect buttons to their respective functions
        self.ui.STUDENTCARS.clicked.connect(self.show_student_cars)
        self.ui.VISITORCARS.clicked.connect(self.show_visitor_cars)
        self.ui.STAFFCARS.clicked.connect(self.show_staff_cars)
        self.ui.searchField.textChanged.connect(self.search_name)  # Add this line

        self.ui.FIRSTRECORD.clicked.connect(self.first_record)
        self.ui.PREVIOUSRECORD.clicked.connect(self.previous_record)
        self.ui.NEXTRECORD.clicked.connect(self.next_record)
        self.ui.LASTRECORD.clicked.connect(self.last_record)

        # Initialize database connection
        self.setup_database()

    def setup_database(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("carpark.db")
        self.db.open()
        self.model = QSqlTableModel()
        self.model.setTable("CarPark")
        self.model.select()
        self.ui.DETAILTABLE.setModel(self.model)

    def show_student_cars(self):
        self.model.setFilter("role='student'")
        self.model.select()

    def show_visitor_cars(self):
        self.model.setFilter("role='visitor'")
        self.model.select()

    def show_staff_cars(self):
        self.model.setFilter("role='staff'")
        self.model.select()

    def first_record(self):
        self.ui.DETAILTABLE.selectRow(0)

    def previous_record(self):
        current_row = self.ui.DETAILTABLE.currentIndex().row()
        if current_row > 0:
            self.ui.DETAILTABLE.selectRow(current_row - 1)

    def next_record(self):
        current_row = self.ui.DETAILTABLE.currentIndex().row()
        if current_row < self.model.rowCount() - 1:
            self.ui.DETAILTABLE.selectRow(current_row + 1)

    def last_record(self):
        self.ui.DETAILTABLE.selectRow(self.model.rowCount() - 1)

    def search_name(self, search_text):
        if " " in search_text:
            first_name, last_name = search_text.split(" ", 1)
            self.model.setFilter(
                f"firstName LIKE '%{first_name}%' AND lastName LIKE '%{last_name}%'"
            )
        else:
            self.model.setFilter(
                f"firstName LIKE '%{search_text}%' OR lastName LIKE '%{search_text}%'"
            )
        self.model.select()


# Run everything
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CarParkApp()
    window.show()
    sys.exit(app.exec_())
