from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from ui import Ui_Dialog
from dbmanager import DBManager, DBViewer


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_manager = DBManager()
        self.db_viewer = DBViewer()

        # Initialize state first
        self.current_records = []
        self.current_index = -1

        # Create tables if they don't exist
        self.db_manager.create_table()

        # Connect search functionality to input fields
        self.FIRSTNAMEINPUT.textChanged.connect(self.search_records)
        self.LASTNAMEINPUT.textChanged.connect(self.search_records)
        self.REGISTRATIONINPUT.textChanged.connect(self.search_records)
        self.MAKEINPUT.textChanged.connect(self.search_records)
        self.MODELINPUT.textChanged.connect(self.search_records)

        # Connect other buttons
        self.STUDENTCARS.clicked.connect(lambda: self.filter_by_role("STUDENT"))
        self.VISITORCARS.clicked.connect(lambda: self.filter_by_role("VISITOR"))
        self.STAFFCARS.clicked.connect(lambda: self.filter_by_role("STAFF"))
        self.SAVEBUTTON.clicked.connect(self.save_record)
        self.CLEARBUTTON.clicked.connect(self.clear_fields)
        self.CLEARSEARCH.clicked.connect(self.clear_search)

        # Initialize table
        self.setup_table()

        # Load initial data
        self.load_all_records()
        self.update_navigation_buttons()

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
        self.DETAILTABLE.setColumnWidth(3, 80)  # Role
        self.DETAILTABLE.setColumnWidth(4, 100)  # Make
        self.DETAILTABLE.setColumnWidth(5, 100)  # Model
        self.DETAILTABLE.setColumnWidth(6, 100)  # Registration

    def search_records(self):
        results = self.db_viewer.search(
            fname=self.FIRSTNAMEINPUT.text() or None,
            lname=self.LASTNAMEINPUT.text() or None,
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
            if not records:
                self.clear_table()
                return

            self.current_records = records
            self.current_index = 0
            self.display_current_record()
            self.update_navigation_buttons()

        except Exception as e:
            self.clear_table()
            QtWidgets.QMessageBox.critical(
                self, "Error", f"Failed to update table: {str(e)}"
            )

    def display_current_record(self):
        self.DETAILTABLE.setRowCount(1)

        if not self.current_records or self.current_index < 0:
            self.clear_table()
            return

        try:
            record = self.current_records[self.current_index]
            for col, value in enumerate(record):
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.DETAILTABLE.setItem(0, col, item)

            self.STATUSLABEL.setText(
                f"Record {self.current_index + 1} of {len(self.current_records)}"
            )
        except IndexError:
            self.clear_table()

    def update_navigation_buttons(self):
        has_records = bool(self.current_records)
        is_first = self.current_index <= 0
        is_final = self.current_index >= len(self.current_records) - 1

        for btn in [
            self.FIRSTRECORD,
            self.PREVIOUSRECORD,
            self.NEXTRECORD,
            self.FINALRECORD,
        ]:
            btn.setEnabled(has_records)

        if has_records:
            self.FIRSTRECORD.setEnabled(not is_first)
            self.PREVIOUSRECORD.setEnabled(not is_first)
            self.NEXTRECORD.setEnabled(not is_final)
            self.FINALRECORD.setEnabled(not is_final)

    def handle_first_click(self):
        if self.current_records:
            self.current_index = 0
            self.display_current_record()
            self.update_navigation_buttons()

    def handle_final_click(self):  # Changed from handle_last_click
        if self.current_records:
            self.current_index = len(self.current_records) - 1
            self.display_current_record()
            self.update_navigation_buttons()

    def handle_next_click(self):
        if self.current_records and self.current_index < len(self.current_records) - 1:
            self.current_index += 1
            self.display_current_record()
            self.update_navigation_buttons()

    def handle_previous_click(self):
        if self.current_records and self.current_index > 0:
            self.current_index -= 1
            self.display_current_record()
            self.update_navigation_buttons()

    def load_all_records(self):
        results = self.db_viewer.search()
        if results:
            self.current_records = results
            self.current_index = 0
            self.display_current_record()
        else:
            self.clear_table()

    def save_record(self):
        try:
            # Get values from input fields
            fname = self.FIRSTNAMEEDIT.text()
            lname = self.LASTNAMEEDIT.text()
            role = self.ROLEEDIT.currentText()
            make = self.MAKEEDIT.text()
            model = self.MODELEDIT.text()
            reg = self.REGISTRATIONEDIT.text()
            date_issued = self.DATEISSUED.date().toString("yyyy-MM-dd")
            date_expiry = self.DATEEXPIRY.date().toString("yyyy-MM-dd")

            # Validate inputs
            if not all([fname, lname, make, model, reg]):
                QtWidgets.QMessageBox.warning(self, "Error", "All fields are required")
                return

            # Confirm before adding
            reply = QtWidgets.QMessageBox.question(
                self,
                "Confirm Add",
                f"Add new permit for {fname} {lname}?\n\nCar: {make} {model}\nReg: {reg}",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No,
            )

            if reply == QtWidgets.QMessageBox.Yes:
                # Insert record
                self.db_manager.insertintotable(
                    fname, lname, role, make, model, reg, date_issued, date_expiry
                )

                # Clear fields and refresh table
                self.clear_fields()
                self.load_all_records()
                QtWidgets.QMessageBox.information(
                    self, "Success", "New permit added successfully"
                )

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def clear_fields(self):
        self.FIRSTNAMEEDIT.clear()
        self.LASTNAMEEDIT.clear()
        self.MAKEEDIT.clear()
        self.MODELEDIT.clear()
        self.REGISTRATIONEDIT.clear()
        self.DATEISSUED.setDate(QtCore.QDate.currentDate())
        self.DATEEXPIRY.setDate(QtCore.QDate.currentDate().addYears(1))

    def clear_search(self):
        """Clear all search fields and reset the view"""
        self.FIRSTNAMEINPUT.clear()
        self.LASTNAMEINPUT.clear()
        self.REGISTRATIONINPUT.clear()
        self.MAKEINPUT.clear()
        self.MODELINPUT.clear()
        self.load_all_records()
        self.update_navigation_buttons()

    def clear_table(self):
        """Clear the table and reset its state"""
        self.DETAILTABLE.setRowCount(0)
        self.current_records = []
        self.current_index = -1
        self.STATUSLABEL.setText("No records found")
        self.update_navigation_buttons()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Collyers Car Park - Permit Management System")
        self.TITLE.setText("Collyers Car Park")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
