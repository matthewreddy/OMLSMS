# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testcount.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testCountDlg(object):
    def setupUi(self, testCountDlg):
        testCountDlg.setObjectName("testCountDlg")
        testCountDlg.resize(346, 299)
        self.widget = QtWidgets.QWidget(testCountDlg)
        self.widget.setGeometry(QtCore.QRect(10, 12, 322, 272))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(18, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(18, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(18, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.prevPushButton = QtWidgets.QPushButton(self.widget)
        self.prevPushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.prevPushButton.setObjectName("prevPushButton")
        self.horizontalLayout_3.addWidget(self.prevPushButton)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.nextPushButton = QtWidgets.QPushButton(self.widget)
        self.nextPushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.nextPushButton.setObjectName("nextPushButton")
        self.horizontalLayout_3.addWidget(self.nextPushButton)
        self.todayPushButton = QtWidgets.QPushButton(self.widget)
        self.todayPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.todayPushButton.setObjectName("todayPushButton")
        self.horizontalLayout_3.addWidget(self.todayPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(18, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.inPushButton = QtWidgets.QPushButton(self.widget)
        self.inPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.inPushButton.setObjectName("inPushButton")
        self.gridLayout.addWidget(self.inPushButton, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.outPushButton = QtWidgets.QPushButton(self.widget)
        self.outPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.outPushButton.setObjectName("outPushButton")
        self.horizontalLayout_2.addWidget(self.outPushButton)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.positivesPushButton = QtWidgets.QPushButton(self.widget)
        self.positivesPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.positivesPushButton.setObjectName("positivesPushButton")
        self.horizontalLayout_2.addWidget(self.positivesPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.resultsPushButton = QtWidgets.QPushButton(self.widget)
        self.resultsPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.resultsPushButton.setObjectName("resultsPushButton")
        self.gridLayout.addWidget(self.resultsPushButton, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.noResultsPushButton = QtWidgets.QPushButton(self.widget)
        self.noResultsPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.noResultsPushButton.setObjectName("noResultsPushButton")
        self.gridLayout.addWidget(self.noResultsPushButton, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.overduePushButton = QtWidgets.QPushButton(self.widget)
        self.overduePushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.overduePushButton.setObjectName("overduePushButton")
        self.horizontalLayout.addWidget(self.overduePushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.closePushButton = QtWidgets.QPushButton(self.widget)
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout_4.addWidget(self.closePushButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(testCountDlg)
        QtCore.QMetaObject.connectSlotsByName(testCountDlg)

    def retranslateUi(self, testCountDlg):
        _translate = QtCore.QCoreApplication.translate
        testCountDlg.setWindowTitle(_translate("testCountDlg", "Dialog"))
        self.label.setText(_translate("testCountDlg", "Count for day of:"))
        self.prevPushButton.setText(_translate("testCountDlg", "<"))
        self.nextPushButton.setText(_translate("testCountDlg", ">"))
        self.todayPushButton.setText(_translate("testCountDlg", "Today"))
        self.label_2.setText(_translate("testCountDlg", "Log counts for the day:"))
        self.label_4.setText(_translate("testCountDlg", "In:"))
        self.inPushButton.setText(_translate("testCountDlg", "(In)"))
        self.label_6.setText(_translate("testCountDlg", "Out:"))
        self.outPushButton.setText(_translate("testCountDlg", "(Out)"))
        self.label_7.setText(_translate("testCountDlg", "Positives:"))
        self.positivesPushButton.setText(_translate("testCountDlg", "(Positives)"))
        self.resultsPushButton.setText(_translate("testCountDlg", "(Results)"))
        self.label_3.setText(_translate("testCountDlg", "tests logged in that day have results"))
        self.noResultsPushButton.setText(_translate("testCountDlg", "(NoResults)"))
        self.label_8.setText(_translate("testCountDlg", "tests logged in that day are awaiting results"))
        self.label_5.setText(_translate("testCountDlg", "Tests overdue for results (all days):"))
        self.overduePushButton.setText(_translate("testCountDlg", "(Overdue)"))
        self.closePushButton.setText(_translate("testCountDlg", "&Close"))