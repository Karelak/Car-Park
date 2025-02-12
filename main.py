from ui import Ui_Dialog
import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class CarPark:
    def __init__(self, ui):
        self.ui = ui
        self.conn = sqlite3.connect("carpark.db")
        self.c = self.conn.cursor()

        # Connect buttons to search
        self.ui.SEARCH.clicked.connect(lambda: self.perform_search(""))
        self.ui.STUDENTCARS.clicked.connect(lambda: self.perform_search("student"))
        self.ui.STAFFCARS.clicked.connect(lambda: self.perform_search("staff"))
        self.ui.VISITORCARS.clicked.connect(lambda: self.perform_search("visitor"))
        self.ui.CLEAR.clicked.connect(self.empty_search)

    def searchDB(self, name, registration, make, model, role):
        # Split the name the user put in into first and last name
        name_parts = name.strip().split(" ", 1)
        fname = name_parts[0] if name_parts else ""
        lname = name_parts[1] if len(name_parts) > 1 else ""
        # MAkes it so that the search is case insensitive and can search for partial input
        fname = f"%{fname}%"
        lname = f"%{lname}%"
        registration = f"%{registration}%"
        make = f"%{make}%"
        model = f"%{model}%"
        role = f"%{role}%"
        # SQL statement to search the database
        self.c.execute(
            """SELECT * FROM Carpark 
               WHERE LOWER(fname) LIKE LOWER(?) 
               AND LOWER(lname) LIKE LOWER(?)
               AND LOWER(registration) LIKE LOWER(?) 
               AND LOWER(make) LIKE LOWER(?) 
               AND LOWER(model) LIKE LOWER(?)
               AND LOWER(role) LIKE LOWER(?)""",
            (fname, lname, registration, make, model, role),
        )
        return self.c.fetchall()

    def perform_search(self, role=""):
        # Get the search terms from the input fields
        name = self.ui.NAMEINPUT.text().strip()
        registration = self.ui.REGISTRATIONINPUT.text().strip()
        make = self.ui.MAKEINPUT.text().strip()
        model = self.ui.MODELINPUT.text().strip()
        # Search the database
        results = self.searchDB(name, registration, make, model, role)
        self.display_results(results)

    # Special case for clear: to be able to just do empty search when pressing the button
    def empty_search(self):
        self.ui.NAMEINPUT.clear()
        self.ui.REGISTRATIONINPUT.clear()
        self.ui.MAKEINPUT.clear()
        self.ui.MODELINPUT.clear()
        self.perform_search("")

    # Get results to the user
    def display_results(self, results):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(
            ["registration", "fname", "lname", "make", "model", "role"]
        )
        # Add the results to the table
        for row in results:
            items = [
                QStandardItem(str(row[0])),
                QStandardItem(str(row[1])),
                QStandardItem(str(row[2])),
                QStandardItem(str(row[3])),
                QStandardItem(str(row[4])),
                QStandardItem(str(row[5])),
            ]
            model.appendRow(items)

        self.ui.DETAILTABLE.setModel(model)


# Run the actual application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    car_park = CarPark(ui)
    Dialog.show()
    sys.exit(app.exec_())
