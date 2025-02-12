from ui import Ui_Dialog
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class CarPark:
    def __init__(self, ui):
        self.ui = ui
        self.conn = sqlite3.connect("carpark.db")
        self.c = self.conn.cursor()

        self.ui.FIRSTRECORD.clicked.connect(self.perform_search)
        self.ui.PREVIOUSRECORD.clicked.connect(self.perform_search)
        self.ui.NEXTRECORD.clicked.connect(self.perform_search)
        self.ui.LASTRECORD.clicked.connect(self.perform_search)

    def searchDB(self, name, registration, make, model):
        name_parts = name.strip().split(" ", 1)
        fname = name_parts[0] if name_parts else ""
        lname = name_parts[1] if len(name_parts) > 1 else ""

        fname = f"%{fname}%"
        lname = f"%{lname}%"
        registration = f"%{registration}%"
        make = f"%{make}%"
        model = f"%{model}%"

        self.c.execute(
            """SELECT * FROM Carpark 
               WHERE LOWER(fname) LIKE LOWER(?) 
               AND LOWER(lname) LIKE LOWER(?)
               AND LOWER(registration) LIKE LOWER(?) 
               AND LOWER(make) LIKE LOWER(?) 
               AND LOWER(model) LIKE LOWER(?)""",
            (fname, lname, registration, make, model),
        )
        return self.c.fetchall()

    def perform_search(self):
        name = self.ui.NAMEINPUT.text().strip()
        registration = self.ui.REGISTRATIONINPUT.text().strip()
        make = self.ui.MAKEINPUT.text().strip()
        model = self.ui.MODELINPUT.text().strip()

        results = self.searchDB(name, registration, make, model)

        self.display_results(results)

    def display_results(self, results):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(
            ["fname", "lname", "registration", "make", "model", "role"]
        )

        for row in results:
            items = [
                QStandardItem(str(row[0])),
                QStandardItem(str(row[1])),
                QStandardItem(str(row[2])),
                QStandardItem(str(row[3])),
                QStandardItem(str(row[4])),
                QStandardItem(str(row[0])),
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
