"""This file renders the starting and sending dialog boxes for
renewals, defining their unique types of behaviors."""
import threading
import datetime
from dateutil.relativedelta import relativedelta
from constants import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
import ui
from printlabeldlg import PrintLabelDlg

from omlweb.models import Renewal, Sterilizer, Dentist, Lot, Test
import djprint
import reportdlg
from finddlg import FindDlg

NUM_TABLE_COLUMNS = 4

class StartRenewalDlg(QDialog, ui.Ui_startRenewalDlg):

    def __init__(self, parent=None):
        super(StartRenewalDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle("Start Renewals")
        
        self.error_initializing = False
        self.lot = None
        self.statusLabel.setText("")
        
        if not self.initializeSterilizers():
            return
        self.initializeSterilizerTable()
        if not self.initializeLots():
            return

    def initializeSterilizers(self):
        """Create the sterilizers to be included in the renewal.
        Some code is duplicated in the overdue report."""
        try:
            sterilizers = Sterilizer.objects.filter(renew=True)
            sterilizers = sterilizers.filter(inactive_date__isnull=True)
            sterilizers = sterilizers.filter(suspend=False)
            sterilizers = sterilizers.filter(dentist__inactive_date__isnull=True)
            self.numberNeedingRenewalLineEdit.setText(str(len(sterilizers)))
        except:
            QMessageBox.information(self, "Database Error", "Error reading database.")
            self.error_initializing = True

        try:
            assert len(sterilizers) != 0
        except:
            QMessageBox.information(self, "No Renewals", "No sterilizers are in need of renewal.")
            self.error_initializing = True
            return False
        try:
            renewals = Renewal.objects.filter(sterilizer__in=sterilizers)
            latest_renewal = {}
            latest_lot = {}
            for renewal in renewals:
                sterilizer_id = RenewalToSterilizerID(renewal.id)
                if not (sterilizer_id in latest_renewal) or \
                latest_lot[sterilizer_id] < RenewalToLotID(renewal.id):
                    latest_lot[sterilizer_id] = RenewalToLotID(renewal.id)
                    if not renewal.inactive_date:
                        latest_renewal[sterilizer_id] = renewal
            latest_renewals = [renewal for key, renewal in latest_renewal.items()]
            tests = Test.objects.filter(renewal_id__in=latest_renewals)
            latest_test = {}
            for test in tests:
                sterilizer_id = RenewalToSterilizerID(test.renewal_id)
                if not (sterilizer_id in latest_test) or \
                    (latest_test[sterilizer_id].renewal_id < test.renewal_id) or \
                    (latest_test[sterilizer_id].renewal_id == test.renewal_id and \
                    latest_test[sterilizer_id].test_num < test.test_num):
                    latest_test[sterilizer_id] = test
            self.sterilizerList = []
            for sterilizer in sterilizers:
                renewal = latest_renewal[sterilizer.id] if sterilizer.id in latest_renewal else None
                test = latest_test[sterilizer.id] if sterilizer.id in latest_test else None
                if renewal:
                    numTests = max(0, renewal.num_tests - (test.test_num if test else 0))
                else:
                    numTests = 0
                self.sterilizerList.append((
                    sterilizer,
                    sterilizer.method,
                    sterilizer.num_tests,
                    latest_lot[sterilizer.id] if renewal else 0,
                    numTests))
            self.sterilizerList.sort(key=lambda tup: tup[3])
        except Exception as e:
            print(e)
            self.error_initializing = True
            return False
        return True
    
    def initializeSterilizerTable(self):
        """Create the table that holds and formats the sterilizers on the renewal."""
        # Edited 4/22/25 to reflect 8c on document
        self.tableWidget.setColumnCount(5)
        labels = ["Sterlizer", "Sterilizer Type","Last Renewal", "Strips", "Tests Remaining"]
        widths = [80,60,40,40,40]

        # Set up behavior to sort table by column header
        header = self.tableWidget.horizontalHeader()
        header.sectionClicked.connect(self.on_header_clicked)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
        self.tableWidget.setSelectionMode(QTableView.ExtendedSelection)

        
        for column, width in enumerate(widths):
            self.tableWidget.setColumnWidth(column, width)
        self.tableWidget.setRowCount(len(self.sterilizerList))
        row = 0
        for sterilizer, method, num, lot, left in self.sterilizerList:
            text = [
                str(sterilizer.id).zfill(STERILIZER_ID_WIDTH),
                str(method.name),
                str(lot),
                str(num),
                str(left)
            ]
            for column in range(0, len(text)):
                    item = QTableWidgetItem(text[column])
                    #item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    item.setTextAlignment(Qt.AlignHCenter)
                    self.tableWidget.setItem(row, column, item)
            row += 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.selectAll()

    def initializeLots(self):
        """Create lots to be used in the renewal."""
        today = datetime.date.today()
        # I think this change accomplishes 8b on the document
        six_months_ago = today - relativedelta(months=6)
        try:
            self.lotList = Lot.objects.filter(inactive_date__isnull=True)
            self.lotList = self.lotList.filter(expiration_date__gte=six_months_ago)
            self.lotList = self.lotList.order_by('-id')
            self.lot = self.lotList[0]
        except Exception as e:
            QMessageBox.information(self, "Database Error", "Error reading database.")
            self.error_initializing = True
        try:
            assert len(self.lotList) != 0
        except Exception as e:
            QMessageBox.warning(self, "No Lots", "No valid lots found for renewal.")
            self.error_initializing = True
            return False
        for number, lot in enumerate(self.lotList):
            self.lotComboBox.insertItem(number, str(lot.id))
        self.lotComboBox.setCurrentIndex(0)
        return True

    def updateCounts(self):
        """Update and replace counts in the database for the renewal."""
        count = 0
        strips = 0
        for row in range(0, len(self.sterilizerList)):
            if self.tableWidget.item(row, 0).isSelected():
                count += 1
                strips += self.sterilizerList[row][2]
        self.renewalsSelectedLineEdit.setText(str(count))
        self.stripsRequiredLineEdit.setText(str(int(strips/DEFAULT_NUM_TESTS)))
    
    def selectLot(self, index):
        """Pinpoint and select the lot specified by the user for the renewal."""
        # Index here is being changed by something somewhere
        # Unsure if this is working correctly but the current code runs without technical error
        index = self.lotComboBox.currentIndex()
        for row in range(0, len(self.sterilizerList)):
            if self.lotList[index].id <= self.sterilizerList[row][2]:
                for col in range(0, NUM_TABLE_COLUMNS):
                    self.tableWidget.item(row, col).setFlags(Qt.NoItemFlags)
                    text = self.tableWidget.item(row, col).text()
                    if text and text[0] != '(':
                        self.tableWidget.item(row, col).setText('(' + text + ')')
            else:
                for col in range(0, NUM_TABLE_COLUMNS):
                    self.tableWidget.item(row, col).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    text = self.tableWidget.item(row, col).text()
                    if text and text[0] == '(':
                        self.tableWidget.item(row, col).setText(text[1:-1])
        self.updateCounts()

    def selectNumRenewals(self, num):
        """Select renewals the specified number of times."""
        i = 0
        index = self.lotComboBox.currentIndex()
        for row in range(0, len(self.sterilizerList)):
            if self.lotList[index].id > self.sterilizerList[row][2]:
                i += 1
                for col in range(0, NUM_TABLE_COLUMNS):
                    self.tableWidget.item(row,col).setSelected(True)
            if i >= num:
                break

    def selectNumStrips(self, num):
        """Select strips the specified number of times."""
        i = 0
        index = self.lotComboBox.currentIndex()
        for row in range(0, len(self.sterilizerList)):
            if self.lotList[index].id > self.sterilizerList[row][2]:
                print(row, i, int(self.sterilizerList[row][0].num_tests/DEFAULT_NUM_TESTS), num)
                if i + int(self.sterilizerList[row][0].num_tests/DEFAULT_NUM_TESTS) <= num:
                    i += int(self.sterilizerList[row][0].num_tests/DEFAULT_NUM_TESTS)
                    for col in range(0, NUM_TABLE_COLUMNS):
                        self.tableWidget.item(row,col).setSelected(True)
            if i == num:
                break
        
    def startRenewal(self, sterilizers):
        """Instantiate the renewal. Method executes upon double click on row in table. """
        lot = self.lotList[self.lotComboBox.currentIndex()]
        
        sortList = [(SterilizerToDentistID(x.id), x) for x in sterilizers]
        sortList.sort()
        list = []
        last_id = SterilizerToDentistID(sortList[0][0])
        list = [sortList[0][1]]
        for id, sterilizer in sortList[1:]:
            if last_id != id:
                list.append(None)
                last_id = id
            list.append(sterilizer)
        names = reportdlg.getDentistNames(list, False)
            
        self.parent().viewText(djprint.printRenewalsStarted(list, names))
        
        # have to do one at a time due to the current barcode printer limitations
        for sterilizer in list:
            if sterilizer:
                dentist = sterilizer.dentist
                self.parent().printHTML(djprint.getRenewalLabelsForSterilizers([sterilizer], [dentist], lot), spawn=False, useLabelPrinter=True)

    # Functions for defining behavior upon pushing buttons.
    @pyqtSlot()
    def on_sendPushButton_clicked(self) -> None:
        self.statusLabel.setText("Printing Renewals")
        # Process events so user sees status update
        QCoreApplication.instance().processEvents()
        sterilizers = []
        for row, data in enumerate(self.sterilizerList):
            if self.tableWidget.item(row, 0).isSelected():
                sterilizers.append(data[0])
        self.startRenewal(sterilizers)

    @pyqtSlot()
    def on_tableWidget_itemSelectionChanged(self) -> None:
        self.updateCounts()

    @pyqtSlot()
    def on_cancelPushButton_clicked(self) -> None:
        self.close()
        
    @pyqtSlot(int)
    def on_lotComboBox_currentIndexChanged(self, index: int) -> None:
        # Not sure if current code acheives intended functionality
        #print(index)
        self.selectLot(index)

    @pyqtSlot()
    def on_renewalsSelectedLineEdit_editingFinished(self) -> None:
        try:
            num = int(self.renewalsSelectedLineEdit.text())
            assert num > 0
            self.tableWidget.clearSelection()
        except:
            pass
        else:
            self.selectNumRenewals(num)
        finally:
            self.tableWidget.setFocus()
            self.updateCounts()

    @pyqtSlot()
    def on_stripsRequiredLineEdit_editingFinished(self) -> None:
        try:
            num = int(self.stripsRequiredLineEdit.text())
            assert num > 0
            self.tableWidget.clearSelection()
        except:
            print("error")
            pass
        else:
            self.selectNumStrips(num)
        finally:
            self.tableWidget.setFocus()
            self.updateCounts()

    @pyqtSlot(int)
    def on_header_clicked(self, index) -> None:
        """Sorts table based on clicking column header. """
        self.tableWidget.sortItems(index)
    
    
    def selectSterilizer(self):
        """Select which sterilizer to be included in the 
        renewal using the find dialog functionality.
        """
        findDlg = FindDlg(
            "Sterilizer",
            self.sterilizerList,
            ["id", "enroll_date"],
            {
            'field_widths': [250, 200],
            'window_height': 400,
            'window_width': 600
            },
            self
            )
        return (findDlg.exec_())


class SendRenewalDlg(QDialog, ui.Ui_sendRenewalDlg):

    def __init__(self, parent=None):
        super(SendRenewalDlg, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle("Send Renewal")
        
        self.statusLabel.setText("Enter or Scan Renewal Number")
        self.numRenewalsLineEdit.setFocus()
        self.printMailingLabelsPushButton.setAutoDefault(False)
        self.printReportsPushButton.setAutoDefault(False)
        self.exitPushButton.setAutoDefault(False)
        self.renewals = []

        self.printMailingLabelsPushButton.setDisabled(True)
        self.printReportsPushButton.setDisabled(True)
        self.mailingLabelsPrinted = False
        self.reportsPrinted = False

        self.error_initializing = False
        self.sterilizers = {}
        self.lots = {}
        today = datetime.date.today()
        try:
            sterilizers = Sterilizer.objects.filter(renew=True)
            sterilizers = sterilizers.filter(inactive_date__isnull=True)
            sterilizers = sterilizers.filter(dentist__inactive_date__isnull=True)
            
            for sterilizer in sterilizers:
                self.sterilizers[sterilizer.id] = sterilizer
            
            lots = Lot.objects.filter(inactive_date__isnull=True)
            lots = lots.filter(expiration_date__gte=today)
            
            for lot in lots:
                self.lots[lot.id] = lot

        except:
            self.error_initializing = True

    def createRenewal(self, sterilizer, lot):
        """Initialize the renewal and set its default values."""
        renewal = Renewal()
        renewal.id = int(str(sterilizer.id) + str(lot.id))
        renewal.sterilizer = sterilizer
        renewal.lot = lot.name
        renewal.renewal_date = datetime.date.today()
        renewal.num_tests = sterilizer.num_tests
        renewal.renewal_fee = sterilizer.renew_fee
        renewal.late_fee = 0
        renewal.payment_date = None
        renewal.payment_amount = None
        renewal.check_num = ""
        renewal.comment = ""
        renewal.inactive_date = None
        return renewal

    def insertIntoDatabase(self, renewal):
        """Save the renewal, translate it into a form that
        can be understood by the database, and store it.
        """
        renewal.save(force_insert=True)
        sterilizer = renewal.sterilizer
        sterilizer.renew = False
        sterilizer.save()

    def getSterilizers(self):
        """Retrieve sterilizers in the same order as
        self.renewals with one access to the database.
        """
        sterilizer_ids = []
        for renewal in self.renewals:
            sterilizer_ids.append(RenewalToSterilizerID(renewal.id))
        sterilizers = Sterilizer.objects.filter(id__in=sterilizer_ids)
        lookup = {}
        for sterilizer in sterilizers:
            lookup[sterilizer.id] = sterilizer
        list = []
        for renewal in self.renewals:
            list.append(lookup[RenewalToSterilizerID(renewal.id)])
        return list
        
    def getDentists(self):
        """Retrieve stored dentists for the renewal."""
        dentist_ids = []
        for renewal in self.renewals:
            dentist_ids.append(RenewalToDentistID(renewal.id))
        list = Dentist.objects.filter(id__in=dentist_ids)
        return list
    
    def printBill(self, renewal):
        """Request a print for the renewal bill."""
        id = RenewalToSterilizerID(renewal.id)
        self.parent().printHTML(djprint.getBillForSterilizer(id))

    def printMailingLabels(self):
        """Request a print for the renewal mailing labels."""
        dentists = self.getDentists()
        labelDlg = PrintLabelDlg(self.parent(), dentists)
        labelDlg.exec_()

    def printReports(self):
        """Request a print for the renewal reports."""
        sterilizers = self.getSterilizers()
        for sterilizer in sterilizers:
            self.parent().printHTML(djprint.getReportForSterilizer(sterilizer.id), spawn=False)

    # Functions for defining behavior upon pushing buttons.
    # Need for find a way to get to bottom of code (add renewal for sterilizer)
    # Also to test print buttons
    @pyqtSlot()
    def on_renewalIdLineEdit_returnPressed(self) -> None:
        text = self.renewalIdLineEdit.text()
        status_text = "Error: Could not add renewal #%s." % text
        try:
            try:
                assert len(text) >= RENEWAL_ID_WIDTH
                assert len(text) <= RENEWAL_ID_WIDTH + STRIP_ID_WIDTH
                if len(text) > RENEWAL_ID_WIDTH:
                    text = text[0:RENEWAL_ID_WIDTH]
                id = int(text)
                sterilizer_id = RenewalToSterilizerID(id)
                lot_id = RenewalToLotID(id)
            except:
                status_text = "Improper ID entered."
                assert False
            
            try:
                # print(self.sterilizers)
                # print(self.lots)
                lot = self.lots[RenewalToLotID(id)]
            except Exception as e:
                # print(e)
                status_text = "Can't use lot number %d." % lot_id
                assert False
            
            try:
                assert not Renewal.objects.filter(id=id)
            except:
                status_text = "Renewal %s already in database." % str(id).zfill(RENEWAL_ID_WIDTH)
                assert False

            try:
                sterilizer = self.sterilizers[RenewalToSterilizerID(id)] 
            except:
                status_text = "Sterilizer %s not up for renewal." % str(sterilizer_id).zfill(STERILIZER_ID_WIDTH)
                assert False

            for renewal in self.renewals:
                if renewal.id == id:
                    status_text = "Renewal %s already added." % str(id).zfill(RENEWAL_ID_WIDTH)
                    assert False
                if RenewalToSterilizerID(renewal.id) == RenewalToSterilizerID(id):
                    status_text = "Renewal for sterilizer %s already added." % str(sterilizer_id).zfill(STERILIZER_ID_WIDTH)
                    assert False
            
            renewal = self.createRenewal(sterilizer, lot)
            self.insertIntoDatabase(renewal)
            self.renewals.append(renewal)
            self.printBill(renewal)
            status_text = "Renewal %s added" % text
            self.printMailingLabelsPushButton.setEnabled(True)
            self.printReportsPushButton.setEnabled(True)
        except:
            QApplication.beep()
        finally:
            self.numRenewalsLineEdit.setText(str(len(self.renewals)))
            self.statusLabel.setText(status_text)
            self.renewalIdLineEdit.setText("")
            self.renewalIdLineEdit.setFocus()

    @pyqtSlot()
    def on_printMailingLabelsPushButton_clicked(self) -> None:
        self.renewalIdLineEdit.releaseKeyboard()
        self.renewalIdLineEdit.setText("")
        self.renewalIdLineEdit.setDisabled(True)
        if self.mailingLabelsPrinted:
            msgBox = QMessageBox()
            ttl = "Already Printed"
            msg = "Mailing labels for the dentist offices have already been" + \
                " sent to the printer.  Do you wish to attempt to send another" + \
                " copy to the printer?"
            if QMessageBox.question(
                self, ttl, msg, QMessageBox.Yes, QMessageBox.No
            ) == QMessageBox.No:
                return

        self.printMailingLabels()
        self.mailingLabelsPrinted = True

    @pyqtSlot()
    def on_printReportsPushButton_clicked(self) -> None:
        self.renewalIdLineEdit.releaseKeyboard()
        self.renewalIdLineEdit.setText("")
        self.renewalIdLineEdit.setDisabled(True)
        if self.reportsPrinted:
            msgBox = QMessageBox()
            ttl = "Already Printed"
            msg = "Reports for the corresponding sterilizers have already been" + \
                " sent to the printer.  Do you wish to attempt to send another" + \
                " copy to the printer?"
            if QMessageBox.question(
                self, ttl, msg, QMessageBox.Yes, QMessageBox.No
            ) == QMessageBox.No:
                return

        self.printReports()
        self.reportsPrinted = True

    @pyqtSlot()
    def on_exitPushButton_clicked(self) -> None:
        self.close()

    def keyPressEvent(self, event):
        """Define behavior to occur upon the pressing of a key.
        We are only paying attention to the Escape key.
        """
        if not event.key() == Qt.Key_Escape:
            super(SendRenewalDlg, self).keyPressEvent(event)
        else:
            self.close()

    def close(self):
        """Define behavior to happen when the dialog is closed."""
        self.renewalIdLineEdit.releaseKeyboard()
        self.renewalIdLineEdit.setDisabled(True)
        close = True
        if self.renewals and not self.mailingLabelsPrinted:
            msgBox = QMessageBox()
            ttl = "Mailing Labels Not Printed"
            msg = "Mailing labels for the dentist offices have not been" + \
                " sent to the printer.  Do you wish exit anyway?"
            if QMessageBox.question(
                self, ttl, msg, QMessageBox.Yes, QMessageBox.No
            ) == QMessageBox.No:
                close = False
        elif self.renewals and not self.reportsPrinted:
            msgBox = QMessageBox()
            ttl = "Reports Not Printed"
            msg = "Reports for the corresponding sterilizers have not been" + \
                " sent to the printer.  Do you wish exit anyway?"
            if QMessageBox.question(
                self, ttl, msg, QMessageBox.Yes, QMessageBox.No
            ) == QMessageBox.No:
                close = False
        if close:
            super(SendRenewalDlg, self).close()
        elif not self.mailingLabelsPrinted and not self.reportsPrinted:
            self.renewalIdLineEdit.setEnabled(True)
            self.renewalIdLineEdit.grabKeyboard()
            self.renewalIdLineEdit.setFocus()