# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(580, 45)
        mainWindow.setMinimumSize(QtCore.QSize(580, 45))
        mainWindow.setMaximumSize(QtCore.QSize(580, 45))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 562, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dentistsPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.dentistsPushButton.setObjectName("dentistsPushButton")
        self.horizontalLayout.addWidget(self.dentistsPushButton)
        self.sterilizersPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.sterilizersPushButton.setObjectName("sterilizersPushButton")
        self.horizontalLayout.addWidget(self.sterilizersPushButton)
        self.lotsPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.lotsPushButton.setObjectName("lotsPushButton")
        self.horizontalLayout.addWidget(self.lotsPushButton)
        self.renewalsPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.renewalsPushButton.setObjectName("renewalsPushButton")
        self.horizontalLayout.addWidget(self.renewalsPushButton)
        self.testsPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.testsPushButton.setObjectName("testsPushButton")
        self.horizontalLayout.addWidget(self.testsPushButton)
        self.reportsPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.reportsPushButton.setObjectName("reportsPushButton")
        self.horizontalLayout.addWidget(self.reportsPushButton)
        self.userComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.userComboBox.setMaximumSize(QtCore.QSize(60, 16777215))
        self.userComboBox.setObjectName("userComboBox")
        self.horizontalLayout.addWidget(self.userComboBox)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.dentistsPushButton.setText(_translate("mainWindow", "&Dentists"))
        self.sterilizersPushButton.setText(_translate("mainWindow", "&Sterilizers"))
        self.lotsPushButton.setText(_translate("mainWindow", "&Lots"))
        self.renewalsPushButton.setText(_translate("mainWindow", "&Renewals"))
        self.testsPushButton.setText(_translate("mainWindow", "&Tests"))
        self.reportsPushButton.setText(_translate("mainWindow", "Re&ports"))