"""This file renders the dialog box for notifying the user
of tests. It helps to establish this behavior based on test criteria."""

import datetime
from constants import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

import ui

from omlweb.models import Dentist, Test
import djprint


class TestNotifyDlg(QDialog, ui.Ui_testNotifyDlg):

    def __init__(self, test, user, pos, parent=None):
        super(TestNotifyDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle("Notify Positive Test Result")
        
        self.test = test
        self.user = user
        self.move(pos)
        # Changed to Test.renewal.id
        dentist_id = str(test.renewal.id).zfill(RENEWAL_ID_WIDTH)[0:DENTIST_ID_WIDTH]
        self.dentist = Dentist.objects.get(id=dentist_id)
        dentist = self.dentist

        self.dentalOfficeLineEdit.setText(dentist.practice_name)
        dentistName = "%s %s %s" % (dentist.title, dentist.fname, dentist.lname)
        self.dentistLineEdit.setText(dentistName)
        contactName = "%s %s %s" % (dentist.contact_title, dentist.contact_fname, 
                                    dentist.contact_lname)
        self.contactPersonLineEdit.setText(contactName)
        self.phoneNumberLineEdit.setText(str(dentist.phone))
        self.faxNumberLineEdit.setText(str(dentist.fax))
        self.emailLineEdit.setText(dentist.email)
        self.comment = None

    # Functions for defining behavior upon pushing buttons.
   
    def on_printNotifiedPushButton_clicked(self) -> None:
        self.parent().printHTML(djprint.printNotifyLetter(self.dentist, self.test, self.user, True))
        self.comment = "Contacted on %s by %s\n" % \
            (RecordDateToText(datetime.date.today()), self.parent().parent().user.initials)
        self.close()

    
    def on_printAttemptedPushButton_clicked(self) -> None:
        self.parent().printHTML(djprint.printNotifyLetter(self.dentist, self.test, self.user, False))
        self.comment = "Contact attempted on %s by %s\n" % \
            (RecordDateToText(datetime.date.today()), self.parent().parent().user.initials)
        self.close()

    
    def on_exitPushButton_clicked(self) -> None:
        self.close()