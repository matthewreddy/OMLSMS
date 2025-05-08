from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_billDlg(object):
    def setupUi(self, billDlg):
        billDlg.setObjectName("billDlg")
        billDlg.resize(226, 166)
        self.widget = QtWidgets.QWidget(billDlg)
        self.widget.setGeometry(QtCore.QRect(8, 8, 120, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.defaultPrintButton = QtWidgets.QRadioButton(self.widget)
        self.defaultPrintButton.setObjectName("defaultPrintButton")
        self.verticalLayout_2.addWidget(self.defaultPrintButton)
        self.wordDocButton = QtWidgets.QRadioButton(self.widget)
        self.wordDocButton.setObjectName("wordDocButton")
        self.verticalLayout_2.addWidget(self.wordDocButton)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.cancelPushButton = QtWidgets.QPushButton(self.widget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_1.addWidget(self.cancelPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_1)

        self.retranslateUi(billDlg)
        QtCore.QMetaObject.connectSlotsByName(billDlg)
    
    def retranslateUi(self, billDlg):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("billDlg", "Specify Bill Format"))
        self.defaultPrintButton.setText(_translate("billDlg", "Print"))
        self.wordDocButton.setText(_translate("billDlg", "To Word"))
        self.cancelPushButton.setText(_translate("billDlg", "E&xit"))