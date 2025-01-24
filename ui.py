from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1125, 750)
        
        # Create main layout widget
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 1071, 691))
        self.layoutWidget.setObjectName("layoutWidget")
        
        # Setup main grid
        self.MAINGRID = QtWidgets.QGridLayout(self.layoutWidget)
        self.MAINGRID.setContentsMargins(0, 0, 0, 0)
        
        self._setup_title()
        self._setup_input_fields()
        self._setup_navigation_buttons()
        self._setup_category_buttons()
        self._setup_detail_table()
        self._setup_image()
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def _create_standard_button(self, text, font_size=12):
        btn = QtWidgets.QPushButton(self.layoutWidget)
        btn.setSizePolicy(self._get_size_policy())
        btn.setFont(self._get_font(font_size))
        btn.setText(text)
        return btn
    
    def _create_standard_input(self):
        input_field = QtWidgets.QLineEdit(self.layoutWidget)
        input_field.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        input_field.setFont(self._get_font(16))
        input_field.setFrame(True)
        return input_field
    
    def _create_standard_label(self, text):
        label = QtWidgets.QLabel(self.layoutWidget)
        label.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        label.setFrameShape(QtWidgets.QFrame.WinPanel)
        label.setText(text)
        return label
    
    def _get_size_policy(self):
        return QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
    
    def _get_font(self, size, bold=False):
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        font.setWeight(75 if bold else 50)
        return font
    
    def _setup_title(self):
        self.TITLE = QtWidgets.QLabel(self.layoutWidget)
        self.TITLE.setFont(self._get_font(34, bold=True))
        self.TITLE.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(85, 170, 255))
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0))
        self.TITLE.setPalette(palette)
        self.MAINGRID.addWidget(self.TITLE, 0, 0, 1, 3)
    
    def _setup_input_fields(self):
        # Create layouts
        self.INPUTLABELS = QtWidgets.QVBoxLayout()
        self.INFOLABELS = QtWidgets.QVBoxLayout()
        
        # Create input fields
        fields = ['NAME', 'REGISTRATION', 'MAKE', 'MODEL']
        for field in fields:
            # Create and add label
            label = self._create_standard_label(field.capitalize())
            setattr(self, f'{field}LABEL', label)
            self.INFOLABELS.addWidget(label)
            
            # Create and add input
            input_field = self._create_standard_input()
            setattr(self, f'{field}INPUT', input_field)
            self.INPUTLABELS.addWidget(input_field)
        
        self.MAINGRID.addLayout(self.INFOLABELS, 1, 0, 1, 1)
        self.MAINGRID.addLayout(self.INPUTLABELS, 1, 1, 1, 1)
    
    def _setup_navigation_buttons(self):
        self.BUTTONS = QtWidgets.QHBoxLayout()
        buttons = ['FIRST', 'LAST', 'NEXT', 'PREVIOUS']
        for button in buttons:
            btn = self._create_standard_button(f"{button.capitalize()} Record")
            setattr(self, f'{button}RECORD', btn)
            # Connect button to its handler
            btn.clicked.connect(getattr(self, f'handle_{button.lower()}_click'))
            self.BUTTONS.addWidget(btn)
        self.MAINGRID.addLayout(self.BUTTONS, 3, 0, 1, 3)
    
    def _setup_category_buttons(self):
        self.SIDEBUTTONS = QtWidgets.QVBoxLayout()
        categories = [('STUDENT', 'Staff'), ('VISITOR', 'Student'), ('STAFF', 'Visitor')]
        for attr, text in categories:
            btn = self._create_standard_button(f"{text} Cars")
            setattr(self, f'{attr}CARS', btn)
            # Connect button to its handler
            btn.clicked.connect(lambda checked, cat=attr.lower(): self.handle_category_click(cat))
            self.SIDEBUTTONS.addWidget(btn)
    
    def _setup_detail_table(self):
        self.SIDEBUTTONSANDTABLE = QtWidgets.QHBoxLayout()
        self.DETAILTABLE = QtWidgets.QTableView(self.layoutWidget)
        self.SIDEBUTTONSANDTABLE.addWidget(self.DETAILTABLE)
        self.SIDEBUTTONSANDTABLE.addLayout(self.SIDEBUTTONS)
        self.MAINGRID.addLayout(self.SIDEBUTTONSANDTABLE, 2, 0, 1, 3)
    
    def _setup_image(self):
        self.IMAGE = QtWidgets.QLabel(self.layoutWidget)
        self.IMAGE.setPixmap(QtGui.QPixmap(".\\../Pictures/Saved Pictures/66u46ummrnp21.png"))
        self.MAINGRID.addWidget(self.IMAGE, 1, 2, 1, 1)
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Dialog")
        self.TITLE.setText("Collyers Car Park")
    
    # Add button handlers
    def handle_first_click(self):
        print("First button clicked")
        # Add your logic here

    def handle_last_click(self):
        print("Last button clicked")
        # Add your logic here

    def handle_next_click(self):
        print("Next button clicked")
        # Add your logic here

    def handle_previous_click(self):
        print("Previous button clicked")
        # Add your logic here

    def handle_category_click(self, category):
        print(f"Category {category} button clicked")
        # Add your logic here


# Run the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())