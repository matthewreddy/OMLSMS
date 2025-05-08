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

    @pyqtSlot()
    def exec_(self) -> None:
        self.passwordLineEdit.setText('test') # todo: change to ''
        self.loginLineEdit.selectAll()
        self.updateUi()
        return super(LoginDlg, self).exec_()

    # Functions for defining behavior upon pushing buttons.
    @pyqtSlot(str)
    def on_loginLineEdit_textEdited(self, text: str) -> None:
        self.updateUi()

    @pyqtSlot()
    def on_loginLineEdit_returnPressed(self) -> None:
        self.passwordLineEdit.setFocus()

    @pyqtSlot(str)
    def on_passwordLineEdit_textEdited(self, text: str) -> None:
        self.updateUi()

    @pyqtSlot()
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

    @pyqtSlot()
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
            settings.DATABASES['default']['USER'] = self.loginLineEdit.text()
            settings.DATABASES['default']['PASSWORD'] = "sinJ4juMper#123"
            #settings.DATABASES['default']['USER'] = 'gray' #'DESKTOP-AC4D5C6\gray1'self.loginLineEdit.text()
            #settings.DATABASES['default']['PASSWORD'] = "12345" #self.passwordLineEdit.text()
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

    @pyqtSlot()
    def on_exitPushButton_clicked(self) -> None:
        self.done(False)
