from ui import Ui_Dialog
from PyQt5 import QtWidgets, QtCore
import sys
import sqlite3
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class CarPark:
    def __init__(self, ui):
        self.ui = ui
        self.conn = sqlite3.connect("carpark.db")
        self.c = self.conn.cursor()
        # self.ui.searchButton.clicked.connect(self.search) # Removed

        # Connect buttons to perform_search method
        self.ui.FIRSTRECORD.clicked.connect(self.perform_search)
        self.ui.PREVIOUSRECORD.clicked.connect(self.perform_search)
        self.ui.NEXTRECORD.clicked.connect(self.perform_search)
        self.ui.LASTRECORD.clicked.connect(self.perform_search)

    def searchDB(self, name, registration, make, model):
        self.c.execute(
            "SELECT * FROM users WHERE fname = ? AND registration = ? AND make = ? AND model = ?",
            (name, registration, make, model),
        )
        return self.c.fetchall()

    def perform_search(self):
        # Get text from input fields
        name = self.ui.NAMEINPUT.text()
        registration = self.ui.REGISTRATIONINPUT.text()
        make = self.ui.MAKEINPUT.text()
        model = self.ui.MODELINPUT.text()

        # Perform the search
        results = self.searchDB(name, registration, make, model)

        # Display the results
        self.display_results(results)

    def display_results(self, results):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(
            ["fname", "registration", "make", "model", "role"]
        )  # Set header labels

        for row in results:
            items = [
                QStandardItem(str(row[0])),  # fname
                QStandardItem(str(row[1])),  # registration
                QStandardItem(str(row[2])),  # make
                QStandardItem(str(row[3])),  # model
                QStandardItem(str(row[4])),  # role
            ]
            model.appendRow(items)

        self.ui.DETAILTABLE.setModel(model)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    car_park = CarPark(ui)
    Dialog.show()
    sys.exit(app.exec_())
