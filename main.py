from ui import Ui_Dialog
from PyQt5 import QtWidgets
import sys
import sqlite3

conn = sqlite3.connect("carpark.db")
c = conn.cursor()


def searchDB(registration, fname, lname, make, model, role):
    query = c.execute(
        """SELECT * FROM CarPark WHERE registration=? AND fname=? AND lname=? AND make=? AND model=? AND role=? """,
        (registration, fname, lname, make, model, role),
    )
    rows = c.fetchall()
    for row in rows:
        print(query)


searchDB("AB12 CDQ", "Jack", "Harris", "Peugeot", "208", "visitor")
# Run ui script
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
