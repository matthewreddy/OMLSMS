# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dentist.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""The following code was generated from the Qt Designer. Every
ui_[blank].py file has a correspinding [blank].ui file. We converted
every UI file from PyQt4 to PyQt 5 as part of our upgrades."""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dentistDlg(object):
    def setupUi(self, dentistDlg):
        dentistDlg.setObjectName("dentistDlg")
        dentistDlg.resize(464, 545)
        self.layoutWidget = QtWidgets.QWidget(dentistDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 443, 527))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.idLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.idLineEdit.setEnabled(False)
        self.idLineEdit.setMaximumSize(QtCore.QSize(61, 20))
        self.idLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.idLineEdit.setObjectName("idLineEdit")
        self.horizontalLayout.addWidget(self.idLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setMaximumSize(QtCore.QSize(46, 16777215))
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)
        self.practiceNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.practiceNameLineEdit.setMaxLength(80)
        self.practiceNameLineEdit.setObjectName("practiceNameLineEdit")
        self.gridLayout_5.addWidget(self.practiceNameLineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(46, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lastNameLineEdit.setMaxLength(80)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.gridLayout.addWidget(self.lastNameLineEdit, 1, 0, 1, 1)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.firstNameLineEdit.setMaxLength(24)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.gridLayout.addWidget(self.firstNameLineEdit, 1, 1, 1, 1)
        self.titleLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.titleLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.titleLineEdit.setMaxLength(6)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.gridLayout.addWidget(self.titleLineEdit, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)
        self.cLastNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.cLastNameLineEdit.setMaxLength(80)
        self.cLastNameLineEdit.setObjectName("cLastNameLineEdit")
        self.gridLayout.addWidget(self.cLastNameLineEdit, 3, 0, 1, 1)
        self.cFirstNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.cFirstNameLineEdit.setMaxLength(24)
        self.cFirstNameLineEdit.setObjectName("cFirstNameLineEdit")
        self.gridLayout.addWidget(self.cFirstNameLineEdit, 3, 1, 1, 1)
        self.cTitleLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.cTitleLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.cTitleLineEdit.setMaxLength(6)
        self.cTitleLineEdit.setObjectName("cTitleLineEdit")
        self.gridLayout.addWidget(self.cTitleLineEdit, 3, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 1, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(46, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(46, 16777215))
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 3, 0, 1, 1)
        self.address1LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.address1LineEdit.setMaxLength(80)
        self.address1LineEdit.setObjectName("address1LineEdit")
        self.gridLayout_5.addWidget(self.address1LineEdit, 3, 1, 1, 1)
        self.address2LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.address2LineEdit.setMaxLength(80)
        self.address2LineEdit.setObjectName("address2LineEdit")
        self.gridLayout_5.addWidget(self.address2LineEdit, 4, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 2, 1, 1)
        self.cityLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.cityLineEdit.setMaxLength(40)
        self.cityLineEdit.setObjectName("cityLineEdit")
        self.gridLayout_2.addWidget(self.cityLineEdit, 1, 0, 1, 1)
        self.stateLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.stateLineEdit.setMaximumSize(QtCore.QSize(41, 16777215))
        self.stateLineEdit.setMaxLength(2)
        self.stateLineEdit.setObjectName("stateLineEdit")
        self.gridLayout_2.addWidget(self.stateLineEdit, 1, 1, 1, 1)
        self.zipLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.zipLineEdit.setMaxLength(10)
        self.zipLineEdit.setObjectName("zipLineEdit")
        self.gridLayout_2.addWidget(self.zipLineEdit, 1, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 1, 1, 1)
        self.phoneLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.phoneLineEdit.setMaxLength(25)
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.gridLayout_3.addWidget(self.phoneLineEdit, 1, 0, 1, 1)
        self.faxLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.faxLineEdit.setMaxLength(25)
        self.faxLineEdit.setObjectName("faxLineEdit")
        self.gridLayout_3.addWidget(self.faxLineEdit, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.emailLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.emailLineEdit.setMaxLength(254)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.verticalLayout_2.addWidget(self.emailLineEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setHorizontalSpacing(18)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)
        self.dateInactivePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.dateInactivePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateInactivePushButton.setObjectName("dateInactivePushButton")
        self.gridLayout_4.addWidget(self.dateInactivePushButton, 0, 1, 1, 1)
        self.enrollDateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.enrollDateEdit.setObjectName("enrollDateEdit")
        self.gridLayout_4.addWidget(self.enrollDateEdit, 1, 0, 1, 1)
        self.dateInactiveLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.dateInactiveLineEdit.setEnabled(False)
        self.dateInactiveLineEdit.setMaximumSize(QtCore.QSize(71, 20))
        self.dateInactiveLineEdit.setMaxLength(12)
        self.dateInactiveLineEdit.setObjectName("dateInactiveLineEdit")
        self.gridLayout_4.addWidget(self.dateInactiveLineEdit, 1, 1, 1, 1)
        self.statusButton = QtWidgets.QLabel(self.layoutWidget)
        self.statusButton.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.statusButton.setObjectName("statusButton")
        self.gridLayout_4.addWidget(self.statusButton,2,0,1,1)
        self.actualStatusButton = QtWidgets.QLabel(self.layoutWidget)
        self.actualStatusButton.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.actualStatusButton.setObjectName("actualStatusButton")
        self.gridLayout_4.addWidget(self.actualStatusButton,2,1,1,1)
        self.horizontalLayout_2.addLayout(self.gridLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.commentTextEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.commentTextEdit.setMaximumSize(QtCore.QSize(16777215, 71))
        self.commentTextEdit.setObjectName("commentTextEdit")
        self.verticalLayout_3.addWidget(self.commentTextEdit)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
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
        self.seekFirstPushButton.setMaximumSize(QtCore.QSize(21, 16777215))
        self.seekFirstPushButton.setObjectName("seekFirstPushButton")
        self.horizontalLayout_5.addWidget(self.seekFirstPushButton)
        self.seekPreviousPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.seekPreviousPushButton.setMaximumSize(QtCore.QSize(21, 16777215))
        self.seekPreviousPushButton.setObjectName("seekPreviousPushButton")
        self.horizontalLayout_5.addWidget(self.seekPreviousPushButton)
        self.seekNextPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.seekNextPushButton.setMaximumSize(QtCore.QSize(21, 16777215))
        self.seekNextPushButton.setObjectName("seekNextPushButton")
        self.horizontalLayout_5.addWidget(self.seekNextPushButton)
        self.seekLastPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.seekLastPushButton.setMaximumSize(QtCore.QSize(21, 16777215))
        self.seekLastPushButton.setObjectName("seekLastPushButton")
        self.horizontalLayout_5.addWidget(self.seekLastPushButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.insertPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.insertPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.insertPushButton.setObjectName("insertPushButton")
        self.horizontalLayout_4.addWidget(self.insertPushButton)
        self.modifyPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.modifyPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.modifyPushButton.setObjectName("modifyPushButton")
        self.horizontalLayout_4.addWidget(self.modifyPushButton)
        self.savePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.savePushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_4.addWidget(self.savePushButton)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_4.addWidget(self.cancelPushButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.labelPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.labelPushButton.setObjectName("labelPushButton")
        self.horizontalLayout_3.addWidget(self.labelPushButton)
        self.billPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.billPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.billPushButton.setObjectName("billPushButton")
        self.horizontalLayout_3.addWidget(self.billPushButton)
        self.reportPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.reportPushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.reportPushButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.reportPushButton.setObjectName("reportPushButton")
        self.horizontalLayout_3.addWidget(self.reportPushButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.retranslateUi(dentistDlg)
        QtCore.QMetaObject.connectSlotsByName(dentistDlg)
        dentistDlg.setTabOrder(self.practiceNameLineEdit, self.lastNameLineEdit)
        dentistDlg.setTabOrder(self.lastNameLineEdit, self.firstNameLineEdit)
        dentistDlg.setTabOrder(self.firstNameLineEdit, self.titleLineEdit)
        dentistDlg.setTabOrder(self.titleLineEdit, self.cLastNameLineEdit)
        dentistDlg.setTabOrder(self.cLastNameLineEdit, self.cFirstNameLineEdit)
        dentistDlg.setTabOrder(self.cFirstNameLineEdit, self.cTitleLineEdit)
        dentistDlg.setTabOrder(self.cTitleLineEdit, self.address1LineEdit)
        dentistDlg.setTabOrder(self.address1LineEdit, self.address2LineEdit)
        dentistDlg.setTabOrder(self.address2LineEdit, self.cityLineEdit)
        dentistDlg.setTabOrder(self.cityLineEdit, self.stateLineEdit)
        dentistDlg.setTabOrder(self.stateLineEdit, self.zipLineEdit)
        dentistDlg.setTabOrder(self.zipLineEdit, self.phoneLineEdit)
        dentistDlg.setTabOrder(self.phoneLineEdit, self.faxLineEdit)
        dentistDlg.setTabOrder(self.faxLineEdit, self.emailLineEdit)
        dentistDlg.setTabOrder(self.emailLineEdit, self.enrollDateEdit)
        dentistDlg.setTabOrder(self.enrollDateEdit, self.commentTextEdit)
        dentistDlg.setTabOrder(self.commentTextEdit, self.dateInactivePushButton)
        dentistDlg.setTabOrder(self.dateInactivePushButton, self.idLineEdit)
        dentistDlg.setTabOrder(self.idLineEdit, self.findPushButton)
        dentistDlg.setTabOrder(self.findPushButton, self.seekFirstPushButton)
        dentistDlg.setTabOrder(self.seekFirstPushButton, self.seekPreviousPushButton)
        dentistDlg.setTabOrder(self.seekPreviousPushButton, self.seekNextPushButton)
        dentistDlg.setTabOrder(self.seekNextPushButton, self.seekLastPushButton)
        dentistDlg.setTabOrder(self.seekLastPushButton, self.insertPushButton)
        dentistDlg.setTabOrder(self.insertPushButton, self.modifyPushButton)
        dentistDlg.setTabOrder(self.modifyPushButton, self.savePushButton)
        dentistDlg.setTabOrder(self.savePushButton, self.cancelPushButton)
        dentistDlg.setTabOrder(self.cancelPushButton, self.labelPushButton)
        dentistDlg.setTabOrder(self.labelPushButton, self.billPushButton)

    def retranslateUi(self, dentistDlg):
        _translate = QtCore.QCoreApplication.translate
        dentistDlg.setWindowTitle(_translate("dentistDlg", "Dialog"))
        self.label.setText(_translate("dentistDlg", "Denstist ID"))
        self.label_18.setText(_translate("dentistDlg", "Practice\n"
"Name"))
        self.label_2.setText(_translate("dentistDlg", "Person In\n"
"Charge"))
        self.label_4.setText(_translate("dentistDlg", "Last Name"))
        self.label_5.setText(_translate("dentistDlg", "First Name"))
        self.label_6.setText(_translate("dentistDlg", "Title"))
        self.label_7.setText(_translate("dentistDlg", "Last Name"))
        self.label_8.setText(_translate("dentistDlg", "First Name"))
        self.label_9.setText(_translate("dentistDlg", "Title"))
        self.label_3.setText(_translate("dentistDlg", "Contact\n"
"Person"))
        self.label_10.setText(_translate("dentistDlg", "Mailing\n"
"Address"))
        self.label_11.setText(_translate("dentistDlg", "City"))
        self.label_12.setText(_translate("dentistDlg", "State"))
        self.label_13.setText(_translate("dentistDlg", "Zip Code"))
        self.label_14.setText(_translate("dentistDlg", "Phone Number"))
        self.label_15.setText(_translate("dentistDlg", "FAX"))
        self.label_16.setText(_translate("dentistDlg", "Email"))
        self.label_17.setText(_translate("dentistDlg", "Enroll Date"))
        self.statusButton.setText(_translate("dentistDlg", "Status: "))
        self.dateInactivePushButton.setText(_translate("dentistDlg", "Date Inactive"))
        self.label_19.setText(_translate("dentistDlg", "Comment"))
        self.findPushButton.setText(_translate("dentistDlg", "&Find"))
        self.seekFirstPushButton.setText(_translate("dentistDlg", "|<"))
        self.seekPreviousPushButton.setText(_translate("dentistDlg", "<"))
        self.seekNextPushButton.setText(_translate("dentistDlg", ">"))
        self.seekLastPushButton.setText(_translate("dentistDlg", ">|"))
        self.insertPushButton.setText(_translate("dentistDlg", "&Insert"))
        self.modifyPushButton.setText(_translate("dentistDlg", "&Modify"))
        self.savePushButton.setText(_translate("dentistDlg", "&Save"))
        self.cancelPushButton.setText(_translate("dentistDlg", "&Cancel"))
        self.labelPushButton.setText(_translate("dentistDlg", "&Label"))
        self.billPushButton.setText(_translate("dentistDlg", "&Bill"))
        self.reportPushButton.setText(_translate("dentistDlg", "Report"))
