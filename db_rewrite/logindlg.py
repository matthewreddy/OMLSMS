"""This file renders the dialog box for logging in."""

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

    # Functions for defining behavior upon pushing buttons.

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
        """Enables buttons when username and password are properly given."""
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
        """Handles logging in.
        Connects to the database, initializes other views,
        and processes events configured to the current user.
        """
        self.statusLabel.setText("Connecting to database...")
        QCoreApplication.instance().processEvents()
        try:
            assert settings.configured
            # Editing the password line must be done
            settings.DATABASES['default']['USER'] = self.loginLineEdit.text() #'DESKTOP-AC4D5C6\gray1'self.loginLineEdit.text()
            settings.DATABASES['default']['PASSWORD'] = "1234" #self.passwordLineEdit.text()
            # this import must be done here to avoid django error
            from updatedatabase import updateDatabase
            # This method can cause trouble when connecting
            updateDatabase()
            self.statusLabel.setText("Performing database maintenance...")
            QCoreApplication.instance().processEvents()
        except Exception as e:
            print(e)
            print(e.args)
            self.statusLabel.setText("Error connecting to database.")
        QCoreApplication.instance().processEvents()
        self.done(True)

    
    def on_exitPushButton_clicked(self) -> None:
        self.done(False)
