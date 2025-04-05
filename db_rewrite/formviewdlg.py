"""This file defines two dialogs: the main parent dialog for
all others, and the form view dialog, which is the parent
of several other dialog boxes.

It defines basic behavior for each dialog, including functions
that should be implemented by its children, as well as functions
that can safely be inherited.
"""

import threading
from constants import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

from finddlg import FindDlg
import printpdf


class MainDlg(QDialog):

    def makeBookmark(self):
        """Generally overwritten by child classes."""
        return {}

    def goToBookmark(self, bookmark):
        """Skeleton. To be overwritten."""
        pass

    def printHTML(self, html, spawn=True, useLabelPrinter=False):
        """Base functionality for rendering HTML."""
        if html:
            try:
                if spawn:
                    thread = threading.Thread(target=printpdf.printHTML, args=(html,useLabelPrinter ))
                    # Start the execution of the thread
                    thread.start()
                else:
                    printpdf.printHTML(html, useLabelPrinter)
            except Exception as e:
                QMessageBox.warning(None, "Print Error.", str(e))

    def printPDF(self, pdf):
        """Base functionality for rendering a PDF."""
        if pdf:
            try:
                thread = threading.Thread(target=printpdf.printPDF, args=(pdf, ))
                # Start the execution of the thread
                thread.start()
            except Exception as e:
                QMessageBox.warning(None, "Print Error.", str(e))

    def viewText(self, text):
        """Base functionality for viewing text."""
        if text:
            try:
                thread = threading.Thread(target=printpdf.viewText, args=(text, ))
                # Start the execution of the thread
                thread.start()
            except Exception as e:
                QMessageBox.warning(None, "View Error.", str(e))

    def printText(self, text):
        """Base functionality for printing text."""
        if text:
            try:
                thread = threading.Thread(target=printpdf.printText, args=(text, ))
                # Start the execution of the thread
                thread.start()
            except Exception as e:
                QMessageBox.warning(None, "Print Error.", str(e))

    def _configValues(self):
        return(self.parent().configValues)
    
    configValues = property(fget=_configValues)


class FormViewDlg(MainDlg):

    def __init__(self, parent=None):
        super(FormViewDlg, self).__init__(parent)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        self.editing = False
        self.inserting = None
        self.orderedByRecordNumber = True

    def initializeModel(self, bookmark={}):
        """Setup initial model."""
        self.loadRecords()
        self.goToBookmark(bookmark)

    def loadRecords(self, record_id=None):
        """Should be defined for child classes.
        Load database records into self.records.
        """
        self.records = []

    def loadForm(self, record):
        """Skeleton. Should be defined for child classes.
        Load data from the record into the form.
        """
        pass
    
    def verifyFormData(self):
        """Skeleton. Should be defined for child classes.
        Verify form data. On error, return a widget with 
        the data that created the violation.
        """
        return None, None

    def saveForm(self, record, id=None):
        """Skeleton. Should be defined for child classes.
        Save form data to the database.
        """
        pass

    def prepareNewRecord(self):
        """Skeleton. Should be defined for child classes.
        Return a 'blank' new record that can be interacted with.
        """
        pass
    
    def getTargetInsertId(self, record):
        """Skeleton. Should be defined for child classes.
        Return the ID to assign for the record when it is inserted.
        """
        return None

    def makeBookmark(self):
        """Skeleton. Should be defined for child classes.
        Return a dictionary containing key information about the current record.
        """
        return {}

    def goToBookmark(self, bookmark):
        """Skeleton. Should be defined for child classes.
        If possible, set the current record in response to the bookmark.
        """
        pass

    def reportNotFound(self, search, type, id):
        """Displays warning if a report cannot be found."""
        msg = "Could not find %s for %s: %s" % (search, type, id)
        QMessageBox.warning(self, "Not Found", msg)

    def saveRecord(self, record, id=None):
        """Save record to the database."""
        widget, message = self.verifyFormData()
        if widget:
            QMessageBox.warning(self, "Data Error", message)
            widget.setFocus()
            return False, widget
        else:
            try:
                self.saveForm(record, id)
                record.save(force_insert=True if self.inserting else False)
            except Exception as e:
                QMessageBox.critical(self, "Save Error", "Could not save to database: %s" % e)
                return False, None
        return True, None

    def getCurrentRecord(self):
        """Return record currently selected."""
        if self.inserting:
            return self.inserting
        else:
            return self.records[self.recordNum]
    
    def setRecordNum(self, value):
        """Initialize record number for record currently selected."""
        if not self.records or not len(self.records):
            self.recordNum = None
        elif self.records and value >= 0 and value < len(self.records):
            self.recordNum = value
            #print(self.recordNum)
            self.loadForm(self.getCurrentRecord())

    def findRecord(self, id):
        """Locate record."""
        if id and self.orderedByRecordNumber:
            for index, record in enumerate(self.records):
                if record.id >= id:
                    self.setRecordNum(index)
                    return
        elif id:
            for index, record in enumerate(self.records):
                if record.id == id:
                    self.setRecordNum(index)
                    return
        self.setRecordNum(0)

    def decrementRecordNum(self):
        """Decrease record number by one."""
        if self.recordNum is not None:
            self.setRecordNum(self.recordNum - 1)

    def incrementRecordNum(self):
        """Increase record number by one."""
        if self.recordNum is not None:
            self.setRecordNum(self.recordNum + 1)

    def disableEditing(self):
        """Set to be read-only."""
        for widget in self.editWidgets:
            widget.setDisabled(True)
        for widget in self.menuWidgets:
            if widget not in self.editFinalizeWidgets:
                widget.setEnabled(True)
            else:
                widget.setDisabled(True)
        self.editing = False
        try:
            self.historyTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        except:
            pass
    
    def enableEditing(self):
        """Allow editing for current form."""
        self.editing = True
        for widget in self.editWidgets:
            widget.setEnabled(True)
        for widget in self.menuWidgets:
            if widget in self.editFinalizeWidgets:
                widget.setEnabled(True)
            else:
                widget.setDisabled(True)
        try:
            self.historyTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        except:
            pass

    def toggleActive(self, id, type, disableMsg, enableMsg):
        """Set whether or not the current form is in focus."""
        msgBox = QMessageBox()
        if not self.inactiveDateIsSet():
            ttl = "Disable %s" % type
            if QMessageBox.question(
                self, ttl, disableMsg, QMessageBox.Yes, QMessageBox.No
            ) == QMessageBox.Yes:
                self.dateInactiveLineEdit.setText(QDate.currentDate().toString("MM/dd/yyyy"))
                success, widget = self.saveRecord(self.getCurrentRecord())
                if success:
                    QMessageBox.information(
                        self, ttl, "%s %s disabled." % (type, id), QMessageBox.Ok
                    )
                self.loadForm(self.getCurrentRecord())
        else:
            ttl = "Enable %s" % type
            if QMessageBox.question(
                self, ttl, enableMsg, QMessageBox.Yes, QMessageBox.No
            ) == QMessageBox.Yes:
                self.dateInactiveLineEdit.clear()
                success, widget = self.saveRecord(self.getCurrentRecord())
                if success:
                    QMessageBox.information(
                        self, ttl, "%s %s enabled." % (type, id), QMessageBox.Ok
                    )
                self.loadForm(self.getCurrentRecord())

    def inactiveDateIsSet(self):
        """Determine whether the set date is inactive."""
        return (len(self.dateInactiveLineEdit.text()) == 10)

    
    def show(self, bookmark={}) -> None:
        """Load the window."""
        try:
            self.initializeModel(bookmark)
        except Exception as e:
            QMessageBox.critical(
                self,
                "Data Error", 
                "Could not load database: %s" % e,
                QMessageBox.Ok
            )
        super(FormViewDlg, self).show()

    # Functions for defining behavior upon pushing buttons.
    @pyqtSlot()
    def on_findPushButton_clicked(self) -> None:
        # Ask user what criteria they would want to search with (only for DentistDlg)
        if self.__class__.__name__ == "DentistDlg":
            msg = AdvancedSearchDialog()
            msg.exec_()

        findDlg = FindDlg(self.windowTitle(), self.records, self.findValues, self.findSizes, self)
        if findDlg:
            self.findRecord(findDlg.exec_())
       
    @pyqtSlot()
    def on_seekFirstPushButton_clicked(self) -> None:
        self.setRecordNum(0)

    @pyqtSlot()
    def on_seekPreviousPushButton_clicked(self) -> None:
        self.decrementRecordNum()

    @pyqtSlot()
    def on_seekNextPushButton_clicked(self) -> None:
        self.incrementRecordNum()

    @pyqtSlot()
    def on_seekLastPushButton_clicked(self) -> None:
        if self.records:
            self.setRecordNum(len(self.records) - 1)

    @pyqtSlot()
    def on_insertPushButton_clicked(self) -> None:
        self.inserting = self.prepareNewRecord()
        if self.inserting:
            self.loadForm(self.inserting)
            self.enableEditing()

    @pyqtSlot()
    def on_modifyPushButton_clicked(self) -> None:
        self.enableEditing()

    @pyqtSlot()
    def on_savePushButton_clicked(self) -> None:
        self.disableEditing()
        if self.inserting:
            id = self.getTargetInsertId(self.inserting)
        else:
            id = None
        success, widget = self.saveRecord(self.getCurrentRecord(), id)
        if not success:
            self.enableEditing()
            if widget:
                widget.setFocus()
        elif self.inserting:
            self.inserting = None
            self.loadRecords(id)

    @pyqtSlot()
    def on_cancelPushButton_clicked(self) -> None:
        self.disableEditing()
        self.inserting = None
        self.loadRecords(self.getCurrentRecord().id)

class FormViewPartialLoadDlg(FormViewDlg):

    def __init__(self, parent=None):
        super(FormViewPartialLoadDlg, self).__init__(parent)

    def loadRecords(self, record_id=None):
        """Partial load records by date to improve initial response time."""
        if record_id:
            self.findRecord(record_id, None)
        self.loadPartialRecords()
        while len(self.records) == 0 \
        and self.getDateRange()[0].year >= DATABASE_START_DATE.year:
            self.decrementDateRange()
            #self.loadPartialRecords()
        while len(self.records) == 0 \
        and self.getDateRange()[0].year <= DATABASE_STOP_DATE.year:
            self.incrementDateRange()
            #self.loadPartialRecords()
        if not record_id:
            self.setRecordNum(len(self.records) - 1)

    # Redefine seek buttons to handle partial loading by month.
    @pyqtSlot()
    def on_seekFirstPushButton_clicked(self) -> None:
        if self.recordNum > 0:
            self.setRecordNum(0)
        else:
            if self.decrementDateRange():
                self.setRecordNum(0)
            else:
                self.incrementDateRange()

    @pyqtSlot()
    def on_seekPreviousPushButton_clicked(self) -> None:
        if self.recordNum > 0:
            self.decrementRecordNum()
        else:
            if self.decrementDateRange():
                self.setRecordNum(len(self.records) - 1)
            else:
                self.incrementDateRange()

    @pyqtSlot()
    def on_seekNextPushButton_clicked(self) -> None:
        if self.records and self.recordNum < len(self.records) - 1:
            self.incrementRecordNum()
        else:
            if self.incrementDateRange():
                self.setRecordNum(0)
            else:
                self.decrementDateRange()

    @pyqtSlot()
    def on_seekLastPushButton_clicked(self) -> None:
        if self.incrementDateRange():
            self.setRecordNum(0)
        else:
            self.decrementDateRange()
            self.setRecordNum(len(self.records) - 1)

    def getDateRange(self):
        """Return date range for the date currently set."""
        return DateRangeForMonth(self.current_year, self.current_month)
    
    def decrementDateRange(self):
        """Decrease the date range by one."""
        if self.current_month > 1:
            self.current_month = self.current_month - 1
        else:
            self.current_year = self.current_year - 1
            self.current_month = 12
        self.loadPartialRecords()
        return self.records
    
    def incrementDateRange(self):
        """Increase the date range by one."""
        month = self.current_month
        year = self.current_year
        if self.current_month < 12:
            self.current_month = self.current_month + 1
        else:
            self.current_year = self.current_year + 1
            self.current_month = 1
        self.loadPartialRecords()
        return self.records

    def findDatedRecord(self, id, date):
        """Locate record by ID and date."""
        if (date.month != self.current_month or date.year != self.current_year):
            self.current_month = date.month
            self.current_year = date.year
            self.loadPartialRecords()
        for index, record in enumerate(self.records):
            if record.id == id:
                self.setRecordNum(index)
                return
        self.setRecordNum(0)

    def findRecord(self, id, record=None):
        """Locate record by ID."""
        if id:
            record_date = self.getRecordDate(id)
            return self.findDatedRecord(id, record_date)

    # Functions for defining behavior upon pushing buttons.
    @pyqtSlot()
    def on_findPushButton_clicked(self) -> None:
        findDlg = FindDlg(self.windowTitle(), self.allRecords, self.findValues, self.findSizes, self)
        if findDlg:
            self.findRecord(findDlg.exec_())

class AdvancedSearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select Additional Feature(s) to search by")
        print(self.windowTitle())
        self.move(200,200)

        layout = QVBoxLayout()

        
        self.cb1 = QCheckBox("Address")
        self.cb2 = QCheckBox("Zip")
        self.cb3 = QCheckBox("State")
        self.cb4 = QCheckBox("Fax")
        self.cb5 = QCheckBox("Phone Number")
        self.cb6 = QCheckBox("Email")
        self.cb7 = QCheckBox("All")

        layout.addWidget(self.cb1)
        layout.addWidget(self.cb2)
        layout.addWidget(self.cb3)

        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.accept)
        layout.addWidget(ok_btn)

        self.setLayout(layout)