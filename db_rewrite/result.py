"""This file renders the dialog box for results. It is used
as a parent to several other child dialog boxes."""

import sys, datetime
from constants import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
import ui

sys.path.append(OMLWEB_PATH)
import djprint

class ResultDlg(QDialog, ui.Ui_resultDlg):

    def __init__(self, dentist, id, parent=None):
        super(ResultDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle("Results for %s - %s" % \
            ("Dentist #" if dentist else "Sterilizer #", 
             str(id).zfill(DENTIST_ID_WIDTH if dentist else STERILIZER_ID_WIDTH)))
        
        self.specificPeriodRadioButton.setChecked(True)
        self.startDateEdit.setDisabled(True)
        self.endDateEdit.setDisabled(True)
        
        self.dentistOffice = dentist
        self.id = id
        
        today = datetime.date.today()
        start = datetime.date(year = today.year, month = 1, day = 1)
        end = datetime.date(year = today.year+1, month = 1, day = 1) - datetime.timedelta(days = 1)
        self.startDateEdit.setDate(start)
        self.startDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(end)
        self.endDateEdit.setCalendarPopup(True)

    # Functions for defining behavior upon pushing buttons.
    @pyqtSlot()
    def on_defaultPeriodRadioButton_clicked(self) -> None:
            if self.specificPeriodRadioButton.isChecked():
                self.specificPeriodRadioButton.setChecked(False)
            self.startDateEdit.setDisabled(True)
            self.endDateEdit.setDisabled(True)

    @pyqtSlot()
    def on_specificPeriodRadioButton_clicked(self) -> None:
            if self.defaultPeriodRadioButton.isChecked():
                self.defaultPeriodRadioButton.setChecked(False)
            self.startDateEdit.setEnabled(True)
            self.endDateEdit.setEnabled(True)

    @pyqtSlot()
    def on_printPushButton_clicked(self) -> None:
        if self.specificPeriodRadioButton.isChecked():
            period = (self.startDateEdit.date().toPyDate(),
                      self.endDateEdit.date().toPyDate())
        else:
            period = None
        if self.dentistOffice:
            html = djprint.getReportForDentist(self.id, period)
            if not html:
                QMessageBox.warning(self, "Not found", "No active sterilizers found for dentist.")
            else:
                self.parent().printHTML(html)
        else:
            self.parent().printHTML(djprint.getReportForSterilizer(self.id, period))
        self.close()

    @pyqtSlot()
    def on_cancelPushButton_clicked(self) -> None:
        self.close()

