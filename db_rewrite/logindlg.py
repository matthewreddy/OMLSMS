import re
from datetime import date
from constants import *


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

import ui
from formviewdlg import MainDlg

import sys
sys.path.append(OMLWEB_PATH)
# sys.path is for the following import,  which can't be done here without
# violating django initialization: from omlweb.models import Dentist
from django.conf import settings
import os


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', "omlweb")
# //

class LoginDlg(MainDlg, ui.Ui_loginDlg):

    def __init__(self, userName=None, parent=None):
        super(LoginDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle("OML Database (Login Required)")
        self.loginPushButton.setFocusPolicy(Qt.NoFocus)
        self.exitPushButton.setFocusPolicy(Qt.NoFocus)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.statusLabel.setText("")
        if userName:
            self.loginLineEdit.setText(userName)

    
    def exec_(self) -> None:
        self.passwordLineEdit.setText('test') # todo: change to ''
        self.loginLineEdit.selectAll()
        self.updateUi()
        return super(LoginDlg, self).exec_()

    
    def on_loginLineEdit_textEdited(self, text: str) -> None:
        self.updateUi()

   
    def on_loginLineEdit_returnPressed(self) -> None:
        self.passwordLineEdit.setFocus()

    
    def on_passwordLineEdit_textEdited(self, text: str) -> None:
        self.updateUi()

    
    def on_passwordLineEdit_returnPressed(self) -> None:
        self.passwordLineEdit.clearFocus()
        if self.loginPushButton.isEnabled:
            self.attemptLogin()

    def updateUi(self):
        login_text = self.loginLineEdit.text()
        password_text = self.passwordLineEdit.text()

        if login_text and password_text:
            enable = True
        else:
            enable = False

        self.loginPushButton.setEnabled(enable)

    
    def on_loginPushButton_clicked(self) -> None:
        self.attemptLogin()

    def attemptLogin(self):
        self.statusLabel.setText("Connecting to database...")
        QCoreApplication.instance().processEvents()
        print("before try")
        try:
            assert settings.configured
            settings.DATABASES['default']['USER'] = self.loginLineEdit.text()
            print(settings.DATABASES['default']['USER'])  #'DESKTOP-AC4D5C6\gray1'self.loginLineEdit.text()
            settings.DATABASES['default']['PASSWORD'] = "1234" #self.passwordLineEdit.text()
            print("after db")
            # this import must be done here to avoid django error
            from updatedatabase import updateDatabase
            updateDatabase()
            print("updated db returned")
            self.statusLabel.setText("Performing database maintenance...")
            QCoreApplication.instance().processEvents()
        except Exception as e:
            print(e)
            print(e.args)
            self.statusLabel.setText("Error connecting to database.")
        QCoreApplication.instance().processEvents()
        print("at the end")
        self.done(True)

    
    def on_exitPushButton_clicked(self) -> None:
        self.done(False)
