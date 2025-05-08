"""This file renders the dialog box for lots. It helps define
behavior for loading and saving records and forms."""

import sys, re
from constants import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

import ui
from formviewdlg import FormViewDlg

sys.path.append(OMLWEB_PATH)
from omlweb.models import Vapor, Lot
from django.db.models import Max


class LotDlg(FormViewDlg, ui.Ui_lotDlg):

    def __init__(self, parent=None):
        super(LotDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle("OMLSMS Lot")

        self.editWidgets = [self.lotNameLineEdit, self.receivedDateEdit,
        self.expirationDateEdit, self.lotCountSpinBox, self.commentLineEdit]
        
        self.menuWidgets = [self.findPushButton, self.seekFirstPushButton,
        self.seekNextPushButton, self.seekPreviousPushButton, self.seekLastPushButton,
        self.insertPushButton, self.modifyPushButton, self.savePushButton,
        self.cancelPushButton, self.dateInactivePushButton]
        
        self.editFinalizeWidgets = [self.savePushButton, self.cancelPushButton]
        
        self.findValues = ["id", "name", "receive_date", "expiration_date", "comment"]
        self.findSizes = {
            'field_widths': [50, 100, 100, 100, 200],
            'window_height': 400,
            'window_width': 600,
            'zfill': [LOT_ID_WIDTH, None, None, None, None],
        }
        self.disableEditing()

    def initializeModel(self, bookmark):
        """Sets up underlying model."""
        if not self.chemicalVaporComboBox.count():
            vapors = Vapor.objects.filter(active=True).order_by("id")
            for vapor in vapors:
                self.chemicalVaporComboBox.insertItem(vapor.id, vapor.name)
        self.loadRecords()
        self.goToBookmark(bookmark)

    def loadRecords(self, record_id=None):
        """Retrieves lot records from database."""
        self.records = Lot.objects.all().order_by("id")
        if record_id:
            self.findRecord(record_id)

    def loadForm(self, record):
        """Retrieves and renders form data."""
        self.idLineEdit.setText(
            str(record.id).zfill(LOT_ID_WIDTH) if record.id else ""
        )
        self.lotNameLineEdit.setText(record.name)
        self.receivedDateEdit.setDate(record.receive_date)
        self.expirationDateEdit.setDate(record.expiration_date)
        self.lotCountSpinBox.setValue(record.count)
        self.chemicalVaporComboBox.setCurrentIndex(record.vapor.id - 1)
        self.dateInactiveLineEdit.setText(RecordDateToText(record.inactive_date))
        self.commentLineEdit.setText(record.comment)
        if record.inactive_date:
            self.dateInactivePushButton.setStyleSheet("background-color: red; color: white;")
        else:
            self.dateInactivePushButton.setStyleSheet("background-color: green; color: white;")

    def verifyFormData(self):
        """Helps verify form data, and displays errors if something is wrong."""
        if self.idLineEdit.text() != "" and \
                not re.match("^\d{%s}$" % LOT_ID_WIDTH, self.idLineEdit.text()):
            return self.idLineEdit, "Lot ID has improper format."
        receive_date = self.receivedDateEdit.date().toPyDate()
        if receive_date.year < 1980:
            return self.enrollDateEdit, "Invalid received date."
        if self.expirationDateEdit.date().toPyDate() < receive_date:
            return self.expirationDateEdit, "Invalid expiration date."
        try:
            Vapor.objects.get(id=self.chemicalVaporComboBox.currentIndex() + 1)
        except:
            return self.methodComboBox, "Can't access Chemical Vapor from database."
        if self.dateInactiveLineEdit.text() != "":
            try:
                assert FormDateToRecord(self.dateInactiveLineEdit.text()) >= receive_date
            except:
                return self.dateInactiveLineEdit, "Invalid inactive date."
        return None, None

    def saveForm(self, record, id=None):
        """Saves the form and stores it in the database."""
        if self.idLineEdit.text():
            assert record.id == int(self.idLineEdit.text())
        else:
            assert record.id == None and self.inserting
            record.id = id
        record.name = self.lotNameLineEdit.text()
        record.receive_date =  self.receivedDateEdit.date().toPyDate()
        record.expiration_date = self.expirationDateEdit.date().toPyDate()
        record.count = self.lotCountSpinBox.value()
        record.vapor = Vapor.objects.get(id=self.chemicalVaporComboBox.currentIndex() + 1)
        record.inactive_date = FormDateToRecord(self.dateInactiveLineEdit.text())
        record.comment = self.commentLineEdit.text()

    def prepareNewRecord(self):
        """Defines behavior for initializing a new record."""
        try:
            default_vapor = Vapor.objects.get(id=DEFAULT_CHEMICAL_VAPOR)
        except:
            return None
        return Lot(
            id = None,
            receive_date = datetime.date.today(),
            expiration_date = datetime.date.today(),
            count = DEFAULT_LOT_COUNT,
            vapor = default_vapor,
        )
    
    def getTargetInsertId(self, record):
        """Find the target ID in which the next item will be inserted."""
        try:
            value = Lot.objects.all().aggregate(Max('id'))['id__max'] + 1
        except:
            return None
        return value

    def makeBookmark(self):
        """Creates a new bookmark based on the ID line."""
        if self.idLineEdit.text():
            return {
                'lot': self.idLineEdit.text()
            }
        return {}

    def goToBookmark(self, bookmark):
        """Navigates to specified bookmark."""
        if 'lot' in bookmark:
            self.findRecord(int(bookmark['lot']))
        else:
            self.findRecord(self.records[len(self.records) - 1].id)

    # Functions for defining behavior upon pushing buttons.
    @pyqtSlot()
    def on_dateInactivePushButton_clicked(self) -> None:
        msgBox = QMessageBox()
        id = self.idLineEdit.text()
        type = "Lot"
        disableMsg = "Disabling will prevent new renewals from using " + \
            "this lot.  Proceed?"
        enableMsg = "Enabling will permit new renewals to use " + \
            "this lot.  Proceed?"
        self.toggleActive(id, type, disableMsg, enableMsg)
