# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lotrecall.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""The following code was generated from the Qt Designer. Every
ui_[blank].py file has a correspinding [blank].ui file. We converted
every UI file from PyQt4 to PyQt 5 as part of our upgrades."""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lotRecallDlg(object):
    def setupUi(self, lotRecallDlg):
        lotRecallDlg.setObjectName("lotRecallDlg")
        lotRecallDlg.resize(266, 79)
        self.widget = QtWidgets.QWidget(lotRecallDlg)
        self.widget.setGeometry(QtCore.QRect(10, 10, 247, 57))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lotComboBox = QtWidgets.QComboBox(self.widget)
        self.lotComboBox.setObjectName("lotComboBox")
        self.horizontalLayout.addWidget(self.lotComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.viewReportPushButton = QtWidgets.QPushButton(self.widget)
        self.viewReportPushButton.setObjectName("viewReportPushButton")
        self.horizontalLayout_2.addWidget(self.viewReportPushButton)
        self.printReportPushButton = QtWidgets.QPushButton(self.widget)
        self.printReportPushButton.setObjectName("printReportPushButton")
        self.horizontalLayout_2.addWidget(self.printReportPushButton)
        self.exitPushButton = QtWidgets.QPushButton(self.widget)
        self.exitPushButton.setObjectName("exitPushButton")
        self.horizontalLayout_2.addWidget(self.exitPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(lotRecallDlg)
        QtCore.QMetaObject.connectSlotsByName(lotRecallDlg)

    def retranslateUi(self, lotRecallDlg):
        _translate = QtCore.QCoreApplication.translate
        lotRecallDlg.setWindowTitle(_translate("lotRecallDlg", "Dialog"))
        self.label.setText(_translate("lotRecallDlg", "List of renewals for lot:"))
        self.viewReportPushButton.setText(_translate("lotRecallDlg", "&View Report"))
        self.printReportPushButton.setText(_translate("lotRecallDlg", "&Print Report"))
        self.exitPushButton.setText(_translate("lotRecallDlg", "E&xit"))
