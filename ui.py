# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carpark.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1125, 750)
        Dialog.setMinimumSize(QtCore.QSize(1125, 750))
        Dialog.setMaximumSize(QtCore.QSize(1125, 750))
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 1071, 691))
        self.layoutWidget.setObjectName("layoutWidget")
        self.MAINGRID = QtWidgets.QGridLayout(self.layoutWidget)
        self.MAINGRID.setContentsMargins(0, 0, 0, 0)
        self.MAINGRID.setObjectName("MAINGRID")
        self.SIDEBUTTONSANDTABLE = QtWidgets.QHBoxLayout()
        self.SIDEBUTTONSANDTABLE.setObjectName("SIDEBUTTONSANDTABLE")
        self.DETAILTABLE = QtWidgets.QTableView(self.layoutWidget)
        self.DETAILTABLE.setObjectName("DETAILTABLE")
        self.SIDEBUTTONSANDTABLE.addWidget(self.DETAILTABLE)
        self.SIDEBUTTONS = QtWidgets.QVBoxLayout()
        self.SIDEBUTTONS.setObjectName("SIDEBUTTONS")
        self.STUDENTCARS = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STUDENTCARS.sizePolicy().hasHeightForWidth())
        self.STUDENTCARS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.STUDENTCARS.setFont(font)
        self.STUDENTCARS.setObjectName("STUDENTCARS")
        self.SIDEBUTTONS.addWidget(self.STUDENTCARS)
        self.VISITORCARS = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VISITORCARS.sizePolicy().hasHeightForWidth())
        self.VISITORCARS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VISITORCARS.setFont(font)
        self.VISITORCARS.setObjectName("VISITORCARS")
        self.SIDEBUTTONS.addWidget(self.VISITORCARS)
        self.STAFFCARS = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STAFFCARS.sizePolicy().hasHeightForWidth())
        self.STAFFCARS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.STAFFCARS.setFont(font)
        self.STAFFCARS.setObjectName("STAFFCARS")
        self.SIDEBUTTONS.addWidget(self.STAFFCARS)
        self.SIDEBUTTONSANDTABLE.addLayout(self.SIDEBUTTONS)
        self.MAINGRID.addLayout(self.SIDEBUTTONSANDTABLE, 2, 0, 1, 3)
        self.BUTTONS = QtWidgets.QHBoxLayout()
        self.BUTTONS.setObjectName("BUTTONS")
        self.FIRSTRECORD = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FIRSTRECORD.sizePolicy().hasHeightForWidth())
        self.FIRSTRECORD.setSizePolicy(sizePolicy)
        self.FIRSTRECORD.setObjectName("FIRSTRECORD")
        self.BUTTONS.addWidget(self.FIRSTRECORD)
        self.NEXTRECORD = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NEXTRECORD.sizePolicy().hasHeightForWidth())
        self.NEXTRECORD.setSizePolicy(sizePolicy)
        self.NEXTRECORD.setObjectName("NEXTRECORD")
        self.BUTTONS.addWidget(self.NEXTRECORD)
        self.LASTRECORD = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LASTRECORD.sizePolicy().hasHeightForWidth())
        self.LASTRECORD.setSizePolicy(sizePolicy)
        self.LASTRECORD.setObjectName("LASTRECORD")
        self.BUTTONS.addWidget(self.LASTRECORD)
        self.PREVIOUSRECORD = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PREVIOUSRECORD.sizePolicy().hasHeightForWidth())
        self.PREVIOUSRECORD.setSizePolicy(sizePolicy)
        self.PREVIOUSRECORD.setObjectName("PREVIOUSRECORD")
        self.BUTTONS.addWidget(self.PREVIOUSRECORD)
        self.MAINGRID.addLayout(self.BUTTONS, 3, 0, 1, 3)
        self.TITLE = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 202, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 202, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 234, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 202, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.TITLE.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.TITLE.setFont(font)
        self.TITLE.setAutoFillBackground(True)
        self.TITLE.setObjectName("TITLE")
        self.MAINGRID.addWidget(self.TITLE, 0, 0, 1, 3)
        self.INPUTLABELS = QtWidgets.QVBoxLayout()
        self.INPUTLABELS.setObjectName("INPUTLABELS")
        self.NAMEINPUT = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NAMEINPUT.sizePolicy().hasHeightForWidth())
        self.NAMEINPUT.setSizePolicy(sizePolicy)
        self.NAMEINPUT.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.NAMEINPUT.setFont(font)
        self.NAMEINPUT.setAutoFillBackground(False)
        self.NAMEINPUT.setText("")
        self.NAMEINPUT.setFrame(True)
        self.NAMEINPUT.setObjectName("NAMEINPUT")
        self.INPUTLABELS.addWidget(self.NAMEINPUT)
        self.REGISTRATIONINPUT = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.REGISTRATIONINPUT.sizePolicy().hasHeightForWidth())
        self.REGISTRATIONINPUT.setSizePolicy(sizePolicy)
        self.REGISTRATIONINPUT.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.REGISTRATIONINPUT.setFont(font)
        self.REGISTRATIONINPUT.setAutoFillBackground(False)
        self.REGISTRATIONINPUT.setFrame(True)
        self.REGISTRATIONINPUT.setObjectName("REGISTRATIONINPUT")
        self.INPUTLABELS.addWidget(self.REGISTRATIONINPUT)
        self.MAKEINPUT = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MAKEINPUT.sizePolicy().hasHeightForWidth())
        self.MAKEINPUT.setSizePolicy(sizePolicy)
        self.MAKEINPUT.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.MAKEINPUT.setFont(font)
        self.MAKEINPUT.setAutoFillBackground(False)
        self.MAKEINPUT.setFrame(True)
        self.MAKEINPUT.setObjectName("MAKEINPUT")
        self.INPUTLABELS.addWidget(self.MAKEINPUT)
        self.MODELINPUT = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MODELINPUT.sizePolicy().hasHeightForWidth())
        self.MODELINPUT.setSizePolicy(sizePolicy)
        self.MODELINPUT.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.MODELINPUT.setFont(font)
        self.MODELINPUT.setAutoFillBackground(False)
        self.MODELINPUT.setFrame(True)
        self.MODELINPUT.setObjectName("MODELINPUT")
        self.INPUTLABELS.addWidget(self.MODELINPUT)
        self.MAINGRID.addLayout(self.INPUTLABELS, 1, 1, 1, 1)
        self.INFOLABELS = QtWidgets.QVBoxLayout()
        self.INFOLABELS.setObjectName("INFOLABELS")
        self.NAMELABEL = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NAMELABEL.sizePolicy().hasHeightForWidth())
        self.NAMELABEL.setSizePolicy(sizePolicy)
        self.NAMELABEL.setAutoFillBackground(False)
        self.NAMELABEL.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.NAMELABEL.setObjectName("NAMELABEL")
        self.INFOLABELS.addWidget(self.NAMELABEL)
        self.REGISTRATIONLABEL = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.REGISTRATIONLABEL.sizePolicy().hasHeightForWidth())
        self.REGISTRATIONLABEL.setSizePolicy(sizePolicy)
        self.REGISTRATIONLABEL.setAutoFillBackground(False)
        self.REGISTRATIONLABEL.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.REGISTRATIONLABEL.setObjectName("REGISTRATIONLABEL")
        self.INFOLABELS.addWidget(self.REGISTRATIONLABEL)
        self.MAKELABEL = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MAKELABEL.sizePolicy().hasHeightForWidth())
        self.MAKELABEL.setSizePolicy(sizePolicy)
        self.MAKELABEL.setAutoFillBackground(False)
        self.MAKELABEL.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.MAKELABEL.setObjectName("MAKELABEL")
        self.INFOLABELS.addWidget(self.MAKELABEL)
        self.MODELABEL = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MODELABEL.sizePolicy().hasHeightForWidth())
        self.MODELABEL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.MODELABEL.setFont(font)
        self.MODELABEL.setAutoFillBackground(False)
        self.MODELABEL.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.MODELABEL.setObjectName("MODELABEL")
        self.INFOLABELS.addWidget(self.MODELABEL)
        self.MAINGRID.addLayout(self.INFOLABELS, 1, 0, 1, 1)
        self.IMAGE = QtWidgets.QLabel(self.layoutWidget)
        self.IMAGE.setText("")
        self.IMAGE.setPixmap(QtGui.QPixmap("../Pictures/Saved Pictures/66u46ummrnp21.png"))
        self.IMAGE.setObjectName("IMAGE")
        self.MAINGRID.addWidget(self.IMAGE, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.STUDENTCARS.setText(_translate("Dialog", "Staff Cars"))
        self.VISITORCARS.setText(_translate("Dialog", "Student Cars"))
        self.STAFFCARS.setText(_translate("Dialog", "Visitor Cars"))
        self.FIRSTRECORD.setText(_translate("Dialog", "First Record"))
        self.NEXTRECORD.setText(_translate("Dialog", "Next Record"))
        self.LASTRECORD.setText(_translate("Dialog", "Last Record"))
        self.PREVIOUSRECORD.setText(_translate("Dialog", "Previous Record"))
        self.TITLE.setText(_translate("Dialog", "Collyers Car Park"))
        self.NAMELABEL.setText(_translate("Dialog", "Name"))
        self.REGISTRATIONLABEL.setText(_translate("Dialog", "Registration"))
        self.MAKELABEL.setText(_translate("Dialog", "Make"))
        self.MODELABEL.setText(_translate("Dialog", "Model"))
