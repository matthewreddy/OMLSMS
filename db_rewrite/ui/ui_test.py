# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""The following code was generated from the Qt Designer. Every
ui_[blank].py file has a correspinding [blank].ui file. We converted
every UI file from PyQt4 to PyQt 5 as part of our upgrades."""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testDlg(object):
    def setupUi(self, testDlg):
        testDlg.setObjectName("testDlg")
        testDlg.resize(502, 517)
        testDlg.setMinimumSize(QtCore.QSize(0, 0))
        testDlg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.layoutWidget = QtWidgets.QWidget(testDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 19, 479, 487))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(13, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.renewalIdLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.renewalIdLineEdit.setEnabled(False)
        self.renewalIdLineEdit.setMaximumSize(QtCore.QSize(91, 20))
        self.renewalIdLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.renewalIdLineEdit.setObjectName("renewalIdLineEdit")
        self.gridLayout.addWidget(self.renewalIdLineEdit, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.testNumLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.testNumLineEdit.setEnabled(False)
        self.testNumLineEdit.setMaximumSize(QtCore.QSize(31, 16777215))
        self.testNumLineEdit.setObjectName("testNumLineEdit")
        self.horizontalLayout_2.addWidget(self.testNumLineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.maxTestNumLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.maxTestNumLineEdit.setEnabled(False)
        self.maxTestNumLineEdit.setMaximumSize(QtCore.QSize(31, 16777215))
        self.maxTestNumLineEdit.setObjectName("maxTestNumLineEdit")
        self.horizontalLayout_2.addWidget(self.maxTestNumLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 4, 1, 1)
        self.renewalDateEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.renewalDateEdit.setEnabled(False)
        self.renewalDateEdit.setMaximumSize(QtCore.QSize(70, 20))
        self.renewalDateEdit.setObjectName("renewalDateEdit")
        self.gridLayout.addWidget(self.renewalDateEdit, 1, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 6, 1, 1)
        self.stripNumLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.stripNumLineEdit.setEnabled(True)
        self.stripNumLineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.stripNumLineEdit.setObjectName("stripNumLineEdit")
        self.gridLayout.addWidget(self.stripNumLineEdit, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setMinimumSize(QtCore.QSize(30, 0))
        self.label_15.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.prevDayPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.prevDayPushButton.setMaximumSize(QtCore.QSize(40, 20))
        self.prevDayPushButton.setObjectName("prevDayPushButton")
        self.gridLayout_3.addWidget(self.prevDayPushButton, 1, 0, 1, 1)
        self.sterilizeDateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.sterilizeDateEdit.setMinimumSize(QtCore.QSize(81, 0))
        self.sterilizeDateEdit.setMaximumSize(QtCore.QSize(81, 16777215))
        self.sterilizeDateEdit.setObjectName("sterilizeDateEdit")
        self.gridLayout_3.addWidget(self.sterilizeDateEdit, 1, 1, 1, 1)
        self.nextDayPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.nextDayPushButton.setMaximumSize(QtCore.QSize(40, 20))
        self.nextDayPushButton.setObjectName("nextDayPushButton")
        self.gridLayout_3.addWidget(self.nextDayPushButton, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.suppliedPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.suppliedPushButton.setEnabled(False)
        self.suppliedPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.suppliedPushButton.setObjectName("suppliedPushButton")
        self.horizontalLayout_7.addWidget(self.suppliedPushButton)
        self.omittedPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.omittedPushButton.setEnabled(False)
        self.omittedPushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.omittedPushButton.setObjectName("omittedPushButton")
        self.horizontalLayout_7.addWidget(self.omittedPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.startDateLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.startDateLineEdit.setMaximumSize(QtCore.QSize(70, 20))
        self.startDateLineEdit.setObjectName("startDateLineEdit")
        self.verticalLayout_4.addWidget(self.startDateLineEdit)
        self.verticalLayout_12.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.resultDateLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.resultDateLineEdit.setMaximumSize(QtCore.QSize(70, 20))
        self.resultDateLineEdit.setObjectName("resultDateLineEdit")
        self.verticalLayout.addWidget(self.resultDateLineEdit)
        self.verticalLayout_12.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.startedByLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.startedByLineEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.startedByLineEdit.setText("")
        self.startedByLineEdit.setObjectName("startedByLineEdit")
        self.verticalLayout_5.addWidget(self.startedByLineEdit)
        self.verticalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.resultsByLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.resultsByLineEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.resultsByLineEdit.setText("")
        self.resultsByLineEdit.setObjectName("resultsByLineEdit")
        self.verticalLayout_6.addWidget(self.resultsByLineEdit)
        self.verticalLayout_11.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.testResultPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.testResultPushButton.setMaximumSize(QtCore.QSize(40, 28))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.testResultPushButton.setFont(font)
        self.testResultPushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.testResultPushButton.setText("")
        self.testResultPushButton.setDefault(False)
        self.testResultPushButton.setFlat(False)
        self.testResultPushButton.setObjectName("testResultPushButton")
        self.gridLayout_2.addWidget(self.testResultPushButton, 1, 0, 1, 1)
        self.controlResultPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.controlResultPushButton.setMaximumSize(QtCore.QSize(40, 28))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.controlResultPushButton.setFont(font)
        self.controlResultPushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.controlResultPushButton.setText("")
        self.controlResultPushButton.setFlat(False)
        self.controlResultPushButton.setObjectName("controlResultPushButton")
        self.gridLayout_2.addWidget(self.controlResultPushButton, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_14.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_14)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.commentTextEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.commentTextEdit.setMinimumSize(QtCore.QSize(431, 0))
        self.commentTextEdit.setMaximumSize(QtCore.QSize(16777215, 71))
        self.commentTextEdit.setObjectName("commentTextEdit")
        self.verticalLayout_8.addWidget(self.commentTextEdit)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.historyTableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.historyTableWidget.setMaximumSize(QtCore.QSize(16777215, 192))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.historyTableWidget.setFont(font)
        self.historyTableWidget.setObjectName("historyTableWidget")
        self.historyTableWidget.setColumnCount(0)
        self.historyTableWidget.setRowCount(0)
        self.verticalLayout_7.addWidget(self.historyTableWidget)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.findPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.findPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.findPushButton.setObjectName("findPushButton")
        self.horizontalLayout_5.addWidget(self.findPushButton)
        self.seekFirstPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.seekFirstPushButton.setMaximumSize(QtCore.QSize(31, 16777215))
        self.seekFirstPushButton.setObjectName("seekFirstPushButton")
        self.horizontalLayout_5.addWidget(self.seekFirstPushButton)
        self.seekPreviousPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.seekPreviousPushButton.setMaximumSize(QtCore.QSize(31, 16777215))
        self.seekPreviousPushButton.setObjectName("seekPreviousPushButton")
        self.horizontalLayout_5.addWidget(self.seekPreviousPushButton)
        self.seekNextPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.seekNextPushButton.setMaximumSize(QtCore.QSize(31, 16777215))
        self.seekNextPushButton.setObjectName("seekNextPushButton")
        self.horizontalLayout_5.addWidget(self.seekNextPushButton)
        self.seekLastPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.seekLastPushButton.setMaximumSize(QtCore.QSize(31, 16777215))
        self.seekLastPushButton.setObjectName("seekLastPushButton")
        self.horizontalLayout_5.addWidget(self.seekLastPushButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout_3.addWidget(self.startPushButton)
        self.resultPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.resultPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.resultPushButton.setObjectName("resultPushButton")
        self.horizontalLayout_3.addWidget(self.resultPushButton)
        self.modifyPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.modifyPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.modifyPushButton.setObjectName("modifyPushButton")
        self.horizontalLayout_3.addWidget(self.modifyPushButton)
        self.savePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.savePushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_3.addWidget(self.savePushButton)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.notifyPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.notifyPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.notifyPushButton.setObjectName("notifyPushButton")
        self.horizontalLayout_4.addWidget(self.notifyPushButton)
        self.reportPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.reportPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.reportPushButton.setObjectName("reportPushButton")
        self.horizontalLayout_4.addWidget(self.reportPushButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.retranslateUi(testDlg)
        QtCore.QMetaObject.connectSlotsByName(testDlg)

    def retranslateUi(self, testDlg):
        _translate = QtCore.QCoreApplication.translate
        testDlg.setWindowTitle(_translate("testDlg", "Dialog"))
        self.label.setText(_translate("testDlg", "Renewal ID"))
        self.label_2.setText(_translate("testDlg", "Test Number"))
        self.label_4.setText(_translate("testDlg", "Renewal Date"))
        self.label_3.setText(_translate("testDlg", "of"))
        self.label_15.setText(_translate("testDlg", "Strip"))
        self.label_5.setText(_translate("testDlg", "Sterilize Date"))
        self.prevDayPushButton.setText(_translate("testDlg", "<"))
        self.nextDayPushButton.setText(_translate("testDlg", ">"))
        self.suppliedPushButton.setText(_translate("testDlg", "Su&pplied"))
        self.omittedPushButton.setText(_translate("testDlg", "&Omitted"))
        self.label_6.setText(_translate("testDlg", "Start Date"))
        self.label_10.setText(_translate("testDlg", "Result Date"))
        self.label_14.setText(_translate("testDlg", "Started By"))
        self.label_12.setText(_translate("testDlg", "Results By"))
        self.label_7.setText(_translate("testDlg", "Results"))
        self.label_8.setText(_translate("testDlg", "Test"))
        self.label_9.setText(_translate("testDlg", "Control"))
        self.label_11.setText(_translate("testDlg", "Comment"))
        self.label_13.setText(_translate("testDlg", "History"))
        self.findPushButton.setText(_translate("testDlg", "&Find"))
        self.seekFirstPushButton.setText(_translate("testDlg", "<<"))
        self.seekPreviousPushButton.setText(_translate("testDlg", "<"))
        self.seekNextPushButton.setText(_translate("testDlg", ">"))
        self.seekLastPushButton.setText(_translate("testDlg", ">>"))
        self.startPushButton.setText(_translate("testDlg", "S&tart"))
        self.resultPushButton.setText(_translate("testDlg", "&Result"))
        self.modifyPushButton.setText(_translate("testDlg", "&Modify"))
        self.savePushButton.setText(_translate("testDlg", "&Save"))
        self.cancelPushButton.setText(_translate("testDlg", "C&ancel"))
        self.notifyPushButton.setText(_translate("testDlg", "&Notify"))
        self.reportPushButton.setText(_translate("testDlg", "R&eport"))
