# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""The following code was generated from the Qt Designer. Every
ui_[blank].py file has a correspinding [blank].ui file. We converted
every UI file from PyQt4 to PyQt 5 as part of our upgrades."""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resultDlg(object):
    def setupUi(self, resultDlg):
        resultDlg.setObjectName("resultDlg")
        resultDlg.resize(226, 166)
        self.widget = QtWidgets.QWidget(resultDlg)
        self.widget.setGeometry(QtCore.QRect(11, 11, 202, 144))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.defaultPeriodRadioButton = QtWidgets.QRadioButton(self.widget)
        self.defaultPeriodRadioButton.setObjectName("defaultPeriodRadioButton")
        self.verticalLayout_2.addWidget(self.defaultPeriodRadioButton)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.specificPeriodRadioButton = QtWidgets.QRadioButton(self.widget)
        self.specificPeriodRadioButton.setObjectName("specificPeriodRadioButton")
        self.verticalLayout.addWidget(self.specificPeriodRadioButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.startDateEdit = QtWidgets.QDateEdit(self.widget)
        self.startDateEdit.setObjectName("startDateEdit")
        self.horizontalLayout_2.addWidget(self.startDateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.endDateEdit = QtWidgets.QDateEdit(self.widget)
        self.endDateEdit.setObjectName("endDateEdit")
        self.horizontalLayout.addWidget(self.endDateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.printPushButton = QtWidgets.QPushButton(self.widget)
        self.printPushButton.setObjectName("printPushButton")
        self.horizontalLayout_3.addWidget(self.printPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(self.widget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(resultDlg)
        # This connects all the signals to slots 
        QtCore.QMetaObject.connectSlotsByName(resultDlg)

    def retranslateUi(self, resultDlg):
        _translate = QtCore.QCoreApplication.translate
        resultDlg.setWindowTitle(_translate("resultDlg", "Dialog"))
        self.label.setText(_translate("resultDlg", "Test Results Report for"))
        self.defaultPeriodRadioButton.setText(_translate("resultDlg", "default time period"))
        self.specificPeriodRadioButton.setText(_translate("resultDlg", "specified time period"))
        self.label_3.setText(_translate("resultDlg", "beginning:"))
        self.label_2.setText(_translate("resultDlg", "and ending:"))
        self.printPushButton.setText(_translate("resultDlg", "&Print"))
        self.cancelPushButton.setText(_translate("resultDlg", "E&xit"))
