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

        # Create tab widget
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.viewTab = QtWidgets.QWidget()
        self.editTab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.viewTab, "View Records")
        self.tabWidget.addTab(self.editTab, "Add New Record")

        # Setup both tabs
        self._setup_view_tab()
        self._setup_edit_tab()

        self.MAINGRID.addWidget(self.tabWidget)
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
        input_field.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        input_field.setFont(self._get_font(16))
        input_field.setFrame(True)
        return input_field

    def _create_standard_label(self, text):
        label = QtWidgets.QLabel(self.layoutWidget)
        label.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        label.setFrameShape(QtWidgets.QFrame.WinPanel)
        label.setText(text)
        return label

    def _get_size_policy(self):
        return QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )

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

    def _setup_input_fields(self):
        # Create layouts
        self.INPUTLABELS = QtWidgets.QVBoxLayout()
        self.INFOLABELS = QtWidgets.QVBoxLayout()

        # Create input fields
        fields = ["FIRSTNAME", "LASTNAME", "REGISTRATION", "MAKE", "MODEL"]
        for field in fields:
            # Create and add label
            label = self._create_standard_label(
                field.title()
            )  # Use title() for nicer display
            setattr(self, f"{field}LABEL", label)
            self.INFOLABELS.addWidget(label)

            # Create and add input
            input_field = self._create_standard_input()
            setattr(self, f"{field}INPUT", input_field)
            self.INPUTLABELS.addWidget(input_field)

    def _setup_navigation_buttons(self):
        self.BUTTONS = QtWidgets.QHBoxLayout()

        # Create navigation buttons in specific order
        nav_buttons = [
            ("FIRST", "First Record"),
            ("PREVIOUS", "Previous"),
            ("NEXT", "Next"),
            ("FINAL", "Final Record"),
        ]

        for attr, text in nav_buttons:
            btn = self._create_standard_button(text)
            setattr(self, f"{attr}RECORD", btn)
            btn.clicked.connect(getattr(self, f"handle_{attr.lower()}_click"))
            self.BUTTONS.addWidget(btn)

    def _setup_category_buttons(self):
        self.SIDEBUTTONS = QtWidgets.QVBoxLayout()
        categories = [
            ("STAFF", "Staff"),
            ("STUDENT", "Student"),
            ("VISITOR", "Visitor"),
        ]
        for attr, text in categories:
            btn = self._create_standard_button(f"{text} Cars")
            setattr(self, f"{attr}CARS", btn)
            # Connect button to its handler
            btn.clicked.connect(
                lambda checked, cat=attr.lower(): self.handle_category_click(cat)
            )
            self.SIDEBUTTONS.addWidget(btn)

    def _setup_detail_table(self):
        self.SIDEBUTTONSANDTABLE = QtWidgets.QHBoxLayout()
        self.DETAILTABLE = QtWidgets.QTableWidget(self.layoutWidget)

        # Set table properties
        self.DETAILTABLE.setAlternatingRowColors(True)
        self.DETAILTABLE.setShowGrid(True)
        self.DETAILTABLE.setStyleSheet("QTableWidget::item { padding: 5px; }")

        # Set size policy to expand
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.DETAILTABLE.setSizePolicy(sizePolicy)

        # Add stretch factor to make table expand
        self.SIDEBUTTONSANDTABLE.addWidget(self.DETAILTABLE, stretch=1)
        self.SIDEBUTTONSANDTABLE.addLayout(self.SIDEBUTTONS)

    def _setup_view_tab(self):
        layout = QtWidgets.QVBoxLayout(self.viewTab)

        self._setup_title()
        layout.addWidget(self.TITLE)

        # Add search section title with minimum height
        searchTitle = QtWidgets.QLabel("Search Records")
        searchTitle.setFont(self._get_font(14, bold=True))
        searchTitle.setMaximumHeight(30)
        layout.addWidget(searchTitle)

        # Make search section compact
        searchLayout = QtWidgets.QHBoxLayout()
        self._setup_input_fields()
        searchLayout.addLayout(self.INFOLABELS)
        searchLayout.addLayout(self.INPUTLABELS)
        layout.addLayout(searchLayout)

        # Make clear search button compact
        self.CLEARSEARCH = self._create_standard_button("Clear Search")
        self.CLEARSEARCH.setMaximumHeight(30)
        layout.addWidget(self.CLEARSEARCH)

        self._setup_category_buttons()
        self._setup_detail_table()
        # Add stretch factor to make table section expand
        layout.addLayout(self.SIDEBUTTONSANDTABLE, stretch=1)

        # Keep status and navigation buttons compact
        self.STATUSLABEL = QtWidgets.QLabel()
        self.STATUSLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.STATUSLABEL.setFont(self._get_font(12))
        self.STATUSLABEL.setMaximumHeight(30)
        layout.addWidget(self.STATUSLABEL)

        self._setup_navigation_buttons()
        layout.addLayout(self.BUTTONS)

    def _setup_edit_tab(self):
        layout = QtWidgets.QVBoxLayout(self.editTab)

        # Add a descriptive label at the top
        addLabel = QtWidgets.QLabel("Add New Parking Permit")
        addLabel.setFont(self._get_font(16, bold=True))
        addLabel.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(addLabel)

        # Add description label
        descLabel = QtWidgets.QLabel("Enter details for the new permit:")
        descLabel.setFont(self._get_font(12))
        layout.addWidget(descLabel)

        # Input fields for new record
        editGrid = QtWidgets.QGridLayout()

        # Person details
        row = 0
        for field in ["First Name", "Last Name"]:
            label = QtWidgets.QLabel(field)
            input_field = self._create_standard_input()
            setattr(self, f"{field.replace(' ', '').upper()}EDIT", input_field)
            editGrid.addWidget(label, row, 0)
            editGrid.addWidget(input_field, row, 1)
            row += 1

        # Role selection
        self.ROLEEDIT = QtWidgets.QComboBox()
        self.ROLEEDIT.addItems(["STUDENT", "STAFF", "VISITOR"])
        editGrid.addWidget(QtWidgets.QLabel("Role"), row, 0)
        editGrid.addWidget(self.ROLEEDIT, row, 1)
        row += 1

        # Car details
        for field in ["Make", "Model", "Registration"]:
            label = QtWidgets.QLabel(field)
            input_field = self._create_standard_input()
            setattr(self, f"{field.upper()}EDIT", input_field)
            editGrid.addWidget(label, row, 0)
            editGrid.addWidget(input_field, row, 1)
            row += 1

        # Date fields
        self.DATEISSUED = QtWidgets.QDateEdit()
        self.DATEEXPIRY = QtWidgets.QDateEdit()
        self.DATEISSUED.setCalendarPopup(True)
        self.DATEEXPIRY.setCalendarPopup(True)
        self.DATEISSUED.setDate(QtCore.QDate.currentDate())
        self.DATEEXPIRY.setDate(QtCore.QDate.currentDate().addYears(1))

        editGrid.addWidget(QtWidgets.QLabel("Date Issued"), row, 0)
        editGrid.addWidget(self.DATEISSUED, row, 1)
        row += 1
        editGrid.addWidget(QtWidgets.QLabel("Date Expiry"), row, 0)
        editGrid.addWidget(self.DATEEXPIRY, row, 1)
        row += 1

        # Action buttons
        buttonLayout = QtWidgets.QHBoxLayout()
        self.SAVEBUTTON = self._create_standard_button("Save Record")
        self.CLEARBUTTON = self._create_standard_button("Clear Fields")
        buttonLayout.addWidget(self.SAVEBUTTON)
        buttonLayout.addWidget(self.CLEARBUTTON)

        layout.addLayout(editGrid)
        layout.addLayout(buttonLayout)

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
