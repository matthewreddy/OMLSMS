"""This file renders the dialog box for dentists, including
their records, bookmarks, and forms associated with them."""

import sys, datetime, re, os
from constants import *

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

import ui
from formviewdlg import FormViewDlg
from printlabeldlg import PrintLabelDlg

sys.path.append(OMLWEB_PATH)
from omlweb.models import Dentist, State
from django.db.models import Max
from django.utils import dateformat
import djprint as djprint
from result import ResultDlg

# Add this to list of libraries required along with openpyxl
import pandas as pd


class DentistDlg(FormViewDlg, ui.Ui_dentistDlg):

    def __init__(self, parent=None):
        super(DentistDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SMS Dentist")
        
        self.enrollDateEdit.setDisplayFormat("MM/dd/yyyy")
        
        self.editWidgets = [self.practiceNameLineEdit, self.lastNameLineEdit,
        self.firstNameLineEdit, self.titleLineEdit, self.cLastNameLineEdit,
        self.cFirstNameLineEdit, self.cFirstNameLineEdit, self.cTitleLineEdit,
        self.address1LineEdit, self.address2LineEdit, self.cityLineEdit, 
        self.stateLineEdit, self.zipLineEdit, self.phoneLineEdit, self.faxLineEdit,
        self.emailLineEdit, self.enrollDateEdit,
        self.commentTextEdit]
        
        self.menuWidgets = [self.findPushButton, self.seekFirstPushButton,
        self.seekNextPushButton, self.seekPreviousPushButton, self.seekLastPushButton,
        self.insertPushButton, self.modifyPushButton, self.savePushButton,
        self.cancelPushButton, self.labelPushButton, self.billPushButton, self.reportPushButton,
        self.dateInactivePushButton,self.actualStatusButton, self.exportPushButton]
        
        self.editFinalizeWidgets = [self.savePushButton, self.cancelPushButton]
        # This determines the fields used in the FindDlg
        self.findValues = ["id", "practice_name", "lname", "fname", "city","state.abbreviation","zip","phone","fax","email"]
        # This determines the sizes allowcated for each find in the FindDlg
        # Must have a list that is as long as the list in findValues for field_widths and zfill
        self.findSizes = {
        'field_widths': [50, 250, 160, 90,90,90,90,90,90,160],
        'window_height': 400,
        'window_width': 600,
        'zfill': [DENTIST_ID_WIDTH, None, None, None,None,None, None, None,None, None],
        }

        self.disableEditing()
        self.lastPhoneNumber = ""
        self.lastFaxNumber = ""
        self.active = False
        
    def loadRecords(self, record_id=None, activeRecords=False):
        """Set records for the dentist."""
        self.records = Dentist.objects.all()
        self.records = self.records.order_by("id")
        # Gets list of all active records (assuming a null inactive date means that the dentist is active)
        if activeRecords:
            self.records = self.records.filter(inactive_date__isnull = True)
        if record_id:
            self.findRecord(record_id)
        # Sets starting index to be 0 
        self.setRecordNum(0)

    def loadForm(self, record):
        """Fill in forms corresponding to the dentist."""
        self.setWindowTitle("SMS Dentist - " + record.getFullName())
        self.idLineEdit.setText(
            str(record.id).zfill(DENTIST_ID_WIDTH) if record.id else ""
        )
        self.practiceNameLineEdit.setText(record.practice_name)
        self.lastNameLineEdit.setText(record.lname)
        self.firstNameLineEdit.setText(record.fname)
        self.titleLineEdit.setText(record.title)
        self.cLastNameLineEdit.setText(record.contact_lname)
        self.cFirstNameLineEdit.setText(record.contact_fname)
        self.cTitleLineEdit.setText(record.contact_title)
        self.address1LineEdit.setText(record.address1)
        self.address2LineEdit.setText(record.address2)
        self.cityLineEdit.setText(record.city)
        self.stateLineEdit.setText(record.state.abbreviation if record.state else "")
        self.zipLineEdit.setText(record.zip)
        self.phoneLineEdit.setText(record.phone)
        self.faxLineEdit.setText(record.fax)
        self.emailLineEdit.setText(record.email)
        self.enrollDateEdit.setDate(QDate(record.enroll_date))
        if record.inactive_date:
            # Sets status to inactive and colors the text red
            self.dateInactiveLineEdit.setText(RecordDateToText(record.inactive_date))
            self.dateInactivePushButton.setStyleSheet("background-color: red; color: white;")
            self.actualStatusButton.setText("Inactive")
            palette = self.actualStatusButton.palette()
            palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
            self.actualStatusButton.setPalette(palette)
        else:
            # Sets status field to active and colors the text green
            self.dateInactiveLineEdit.setText("")
            self.dateInactivePushButton.setStyleSheet("background-color: green; color: white;")
            self.actualStatusButton.setText("Active")
            palette = self.actualStatusButton.palette()
            palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
            self.actualStatusButton.setPalette(palette)
        self.commentTextEdit.setText(record.comment)
    
    def verifyFormData(self):
        """Ensures form input is valid before saving."""
        if self.idLineEdit.text() != "" and \
                not re.match(r"^\d{%s}$" % DENTIST_ID_WIDTH, self.idLineEdit.text()):
            return self.idLineEdit, "Dentist ID has improper format."
        if self.practiceNameLineEdit.text() == "" and \
                self.lastNameLineEdit.text() == "":
            return self.practiceNameLineEdit, "Enter practice or dentist name."
        if self.address1LineEdit.text() == "" and \
                self.address2LineEdit.text() == "":
            return self.address1LineEdit, "Enter address."
        if self.cityLineEdit.text() == "":
            return self.cityLineEdit, "Enter city."
        try:
            self.stateLineEdit.setText(self.stateLineEdit.text().upper())
            State.objects.get(abbreviation=self.stateLineEdit.text().upper())
        except Exception as e:
            print(e)
            return self.stateLineEdit, "Can't find state in database."
        if not re.match(r"^\d{5}(-\d{4})?$", self.zipLineEdit.text()):
            return self.zipLineEdit, "Improper ZIP code."
        if not re.match(r"^\d{3}-\d{3}-\d{4}(/\d*)?$", self.phoneLineEdit.text()):
            return self.phoneLineEdit, "Improper phone number."
        if self.faxLineEdit.text() != "" and \
            not re.match(r"^\d{3}-\d{3}-\d{4}(/\d*)?$", self.faxLineEdit.text()):
            return self.faxLineEdit, "Improper phone number."
        if self.emailLineEdit.text() and \
            not re.match(r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$",
            self.emailLineEdit.text()
        ):
            return self.emailLineEdit, "Improper E-mail address."
        enroll_date = self.enrollDateEdit.date().toPyDate()
        if enroll_date.year < 1980:
            return self.enrollDateEdit, "Invalid enroll date."
        if self.dateInactiveLineEdit.text() != "":
            try:
                inactive = FormDateToRecord(self.dateInactiveLineEdit.text())
                assert inactive >= enroll_date
            except:
                return self.dateInactiveLineEdit, "Invalid inactive date."
        return None, None

    def saveForm(self, record, id=None):
        """Save form to the dentist's profile."""
        if self.idLineEdit.text():
            assert record.id == int(self.idLineEdit.text())
        else:
            assert record.id == None and self.inserting
            record.id = id
        record.practice_name = self.practiceNameLineEdit.text()
        record.lname = self.lastNameLineEdit.text()
        record.fname = self.firstNameLineEdit.text()
        record.title = self.titleLineEdit.text()
        record.contact_lname = self.cLastNameLineEdit.text()
        record.contact_fname = self.cFirstNameLineEdit.text()
        record.contact_title = self.cTitleLineEdit.text()
        record.address1 = self.address1LineEdit.text()
        record.address2 = self.address2LineEdit.text()
        record.city = self.cityLineEdit.text()
        record.state = State.objects.get(abbreviation=self.stateLineEdit.text())
        record.zip = self.zipLineEdit.text()
        record.phone = self.phoneLineEdit.text()
        record.fax = self.faxLineEdit.text()
        record.email = self.emailLineEdit.text()
        record.enroll_date = self.enrollDateEdit.date().toPyDate()
        record.inactive_date = FormDateToRecord(self.dateInactiveLineEdit.text())
        record.comment = self.commentTextEdit.toPlainText()

    def prepareNewRecord(self):
        """Helper function for loading new record."""
        return Dentist(
        id=None,
        state=State.objects.get(abbreviation="NC"),
        enroll_date = datetime.date.today()
        )

    def getTargetInsertId(self, record):
        """Find the next valid place to insert something within the dentist's profile."""
        try:
            value = Dentist.objects.all().aggregate(Max('id'))['id__max'] + 1
        except:
            return None
        return value

    def makeBookmark(self):
        """Save a bookmark under the dentist's profile."""
        if re.match(r"^\d{%s}$" % DENTIST_ID_WIDTH, self.idLineEdit.text()):
            return {'dentist': self.idLineEdit.text()}

    def goToBookmark(self, bookmark):
        """Locate a bookmark under the dentist's profile."""
        if 'dentist' in bookmark:
            self.findRecord(int(bookmark['dentist']))
        else:
            self.findRecord(None)

    def findRecord(self, id):
        """Locate a record under the dentist's profile."""
        for index, record in enumerate(self.records):
            if record.id == id:
                self.setRecordNum(index)
                return
        self.setRecordNum(0)

    # Functions for defining behavior upon pushing buttons.
    @pyqtSlot()
    def on_dateInactivePushButton_clicked(self) -> None:
        msgBox = QMessageBox()
        id = self.idLineEdit.text()
        type = "Dentist"
        disableMsg = "Disabling this dentist will disable all associated sterilizers" + \
            " and renewals.  Proceed?"
        enableMsg = "Enabling this dentist will enable all associated sterilizers" + \
            " and renewals that were not individually disabled.  Proceed?"
        toggled = self.toggleActive(id, type, disableMsg, enableMsg)

    @pyqtSlot()
    def on_labelPushButton_clicked(self) -> None:
        labelDlg = PrintLabelDlg(self)
        labelDlg.exec_()

    @pyqtSlot()
    def on_billPushButton_clicked(self) -> None:
        html = djprint.getBillsForDentist(self.getCurrentRecord())
        if not html:
            QMessageBox.warning(self, "Not found", "No active sterilizers found for dentist.")
        else:
            self.printHTML(html)

    @pyqtSlot(str)
    def on_phoneLineEdit_textChanged(self, newText: str) -> None:
        self.lastPhoneNumber = self.phoneLineEdit.text()

    @pyqtSlot(str)
    def on_phoneLineEdit_textEdited(self, newText: str) -> None:
        self.numberEdited(self.phoneLineEdit, newText, self.lastPhoneNumber)

    @pyqtSlot()
    def on_reportPushButton_clicked(self) -> None:
        id = self.idLineEdit.text()
        dlg = ResultDlg(True, id, self)
        dlg.exec_()

    @pyqtSlot(str)
    def on_faxLineEdit_textChanged(self, newText:str) -> None:
        self.lastFaxNumber = self.faxLineEdit.text()

    @pyqtSlot(str)
    def on_faxLineEdit_textEdited(self, newText:str) -> None:
        self.numberEdited(self.faxLineEdit, newText, self.lastFaxNumber)
    
    @pyqtSlot(int)
    def on_activeDentists_stateChanged(self, state: int) -> None:
        # State = 2 = checked
        # State = 0 = not checked
        # Reload active records and set global flag for export
        if state != 0:
            self.active = True
            self.loadRecords(None, True)
        else:
            self.active = False
            self.loadRecords(None, False)

    @pyqtSlot()
    def on_exportPushButton_clicked(self) -> None:
        df = pd.DataFrame()
        # Loop through records and append to df such that each record is a row
        for record in self.records:
            data = {'Practice Name' : record.practice_name,
                    'Title' : record.title,
                    'First Name' : record.fname,
                    'Last Name': record.lname,
                    'Contact Title': record.contact_title,
                    'Contact First Name' : record.contact_fname,
                    'Contact Last Name' : record.contact_lname,
                    'Address1': record.address1,
                    'Address2': record.address2,
                    'City' : record.city,
                    'State': record.state.abbreviation,
                    'Zip' : record.zip,
                    'Phone' : record.phone,
                    'Fax' : record.fax,
                    'Email' : record.email,
                    'Enroll Date' : dateformat.format(record.enroll_date, 'Y-m-d'),
                    'Inactive Date' : dateformat.format(record.inactive_date, 'Y-m-d') if record.inactive_date else "N/A"}
            new_row = pd.DataFrame([data])
            df = pd.concat([df,new_row])
        today = datetime.datetime.today().date().isoformat()
        if self.active:
            path = today + "Active Dentist List.xlsx"
        else:
            path = today + " Dentist List.xlsx"
    
        # Creates excel file
        df.to_excel(path, index=False)

        # Open file on computer
        os.startfile(path)

    def numberEdited(self, sender, text, oldText):
        # in most positions, undo last entry unless it is a digit
        if len(text) not in [0,4,8] and len(text)<13:
            if not str(text[-1]).isdigit():
                sender.setText(text[0:-1])
                return
        # if we came forward to position followed by a dash, add it automatically
        if len(text) in [3,7] and len(oldText) in [2,6]:
            sender.setText(text + "-")
        # if we deleted a dash to come to number before it, delete that number
        elif len(text) in [3,7] and len(oldText) in [4,8]:
            sender.setText(text[0:-1])
        # allow anything after a slash for extensions
        elif len(text) > 12 and text[12] != '/':
            sender.setText(text[0:12] + '/' + text[12:])


