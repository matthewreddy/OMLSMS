"""This file renders the dialog box for searching/finding,
defining behavior for filtering and populating the browser
under certain criteria."""

import datetime
from constants import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

class FindDlg(QDialog):
 
    def __init__(self, title, records, fields, sizes, parent=None):
        super(FindDlg, self).__init__(parent)
        self.setWindowModality(Qt.WindowModal)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.WindowTitleHint)
        self.setWindowTitle("Find " + title)
        
        self.unfiltered_records = records
        self.records = records
        self.fields = fields
        self.sizes = sizes
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.populateBrowser(fields, records)
        self.buildDisplay()
        self.filterLineEdit.setFocus()
        self.selectPushButton.setDisabled(True)
        
        # connect signals to slots
        self.filterLineEdit.textChanged.connect(self.on_filterLineEdit_textChanged)
        self.filterLineEdit.returnPressed.connect(self.on_filterLineEdit_returnPressed)
        self.filterPushButton.clicked.connect(self.on_filterPushButton_clicked)
        self.tableWidget.itemClicked.connect(self.on_tableWidget_itemClicked)
        self.tableWidget.itemDoubleClicked.connect(self.on_tableWidget_itemDoubleClicked)
        self.selectPushButton.clicked.connect(self.on_selectPushButton_clicked)
        self.cancelPushButton.clicked.connect(self.on_cancelPushButton_clicked)


    def filterData(self):
        """Filter returned data based on criteria provided in the fields."""
        text = self.filterLineEdit.text()
        if not text:
            return
        if self.sizes['zfill'][0]:
            idtext = text[0:self.sizes['zfill'][0]]
            # Changed to idtext and idtext[0] with changes to filter on every keystroke
            while idtext and idtext[0] == '0':
                idtext = idtext[1:]
        filter = self.fields[0].replace(".", "__") + '__startswith'
        self.records = self.unfiltered_records.filter(**{ filter: idtext })
        for column in range(1, len(self.fields)):
            filter = self.fields[column].replace(".", "__") + '__startswith'
            self.records = self.records | self.unfiltered_records.filter(**{ filter: self.filterLineEdit.text() })
        # if records is only one record switch to that recod
        if len(self.records) == 1:
            self.done(getattr(self.records[0], "id", None))
        self.populateBrowser(self.fields, self.records)

    def populateBrowser(self, fields, records):
        """Populate the browser with results from find."""
        self.tableWidget.setDisabled(True)
        self.tableWidget.verticalHeader().hide()
        if records.count() > MAX_FIND_DISPLAY_ROWS:
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setRowCount(1)
            item = QTableWidgetItem("Too many items to display.  Use filter to search by ID number.")
            item.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(0, 0, item)
            self.tableWidget.setRowHeight(0, self.sizes['window_height'] - 88)
            self.tableWidget.setColumnWidth(0, self.sizes['window_width'] - 27)
        elif records.count() == 0:
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setRowCount(1)
            item = QTableWidgetItem("No matches found.")
            item.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(0, 0, item)
            self.tableWidget.setRowHeight(0, self.sizes['window_height'] - 88)
            self.tableWidget.setColumnWidth(0, self.sizes['window_width'] - 27)
        else:
            columns = len(fields)
            rows = len(records)
            self.tableWidget.setColumnCount(columns)
            self.tableWidget.setRowCount(rows)

            # Check which parent is calling FindDlg and set headers appropriately
            if self.parent().__class__.__name__ == "DentistDlg":
                self.tableWidget.setHorizontalHeaderLabels(["ID", "Practice Name", "Last Name", 
                                                       "First Name", "City", "State", "Zipcode", "Phone", "Fax", "Email"])
            elif self.parent().__class__.__name__ == "SterilizerDlg":
                self.tableWidget.setHorizontalHeaderLabels(["ID", "Enroll Date", "Comment"])
            elif self.parent().__class__.__name__ == "LotDlg":
                self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Receive Date", "Expiration Date", "Comment"])  
            # Searching Renewal Objcts in both RenewalDlg and TestDlg
            elif self.parent().__class__.__name__ == "RenewalDlg" or self.parent().__class__.__name__ == "TestDlg":
                self.tableWidget.setHorizontalHeaderLabels(["Renewal ID", "Lot", "Renewal Date"])
            
            # Header styling

            # Makes font bold
            header = self.tableWidget.horizontalHeader()
            font = header.font()
            font.setBold(True)
            header.setFont(font)
            
            # Make bottom border 
            self.tableWidget.setStyleSheet("""
                QHeaderView::section {
                    background-color: white;
                    color: black;
                    border: none;
                    border-bottom: 1px solid #444;  
                    padding: 4px;
                }
                """)
            
            # This could potentially be improved for performance in the future
            for column in range(columns):
                for row in range(rows):
                    if "." in fields[column]:
                        # Unsure of purpose of temp and rec
                        temp = fields[column].split(".")
                        rec = getattr(records[row], temp[0], "")
                        # For advanced search, if rec is a State object
                        # , set value to be abbreviation

                        # import must be done here to avoid django error
                        sys.path.append(OMLWEB_PATH)
                        from omlweb.models import State
                        if isinstance(rec, State):
                            value = rec.abbreviation
                        else:
                            value = getattr(records[row], temp[1], "")
                    else:
                        value = getattr(records[row], fields[column], "")
                    if isinstance(value, int):
                        if self.sizes['zfill'][column]:
                            value = str(value).zfill(self.sizes['zfill'][column])
                        else:
                            value = str(value)
                    elif isinstance(value, datetime.date):
                        value = RecordDateToText(value)
                    item = QTableWidgetItem(NullNone(value))
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.tableWidget.setItem(row, column, item)

            if columns > 0:
                self.tableWidget.setRowHeight(0, 30)
            for column in range(columns):
                width = self.sizes['field_widths'][column]
                self.tableWidget.setColumnWidth(column, width)
            self.tableWidget.setEnabled(True)
            self.tableWidget.setSelectionBehavior(QTableView.SelectRows)


    def buildDisplay(self):
        """Lays out the form manually. This is done to help
        the form be more adaptive to the results.
        Note that no .ui file exists for this dialog.
        """
        self.search_label = QLabel("Search:")
        self.filterLineEdit = QLineEdit(self)
        self.filterPushButton = QPushButton(self)
        self.filterPushButton.setText("&Filter")
        self.filterPushButton.setFocusPolicy (Qt.NoFocus)
        self.selectPushButton = QPushButton(self)
        self.selectPushButton.setText("&Select")
        self.selectPushButton.setFocusPolicy (Qt.NoFocus)
        self.cancelPushButton = QPushButton(self)
        self.cancelPushButton.setText("&Cancel")
        self.cancelPushButton.setFocusPolicy (Qt.NoFocus)
        self.cross_layout = QHBoxLayout()
        self.cross_layout.addStretch()
        self.cross_layout.addWidget(self.search_label)
        self.cross_layout.addWidget(self.filterLineEdit)
        self.cross_layout.addWidget(self.filterPushButton)
        self.cross_layout.addStretch()
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addStretch()
        self.bottom_layout.addWidget(self.selectPushButton)
        self.bottom_layout.addWidget(self.cancelPushButton)
        self.bottom_layout.addStretch()
        
        layout = QVBoxLayout()
        layout.addLayout(self.cross_layout)
        layout.addWidget(self.tableWidget)
        layout.addLayout(self.bottom_layout)
        self.resize(self.sizes['window_width'], self.sizes['window_height'])
        self.setLayout(layout)

    def getSelectedId(self):
        """Returns specific ID selected by the user."""
        row = self.tableWidget.currentRow()
        if row >= 0:
            return getattr(self.records[row], "id", None)
        else:
            return None

    # Functions for defining behavior upon pushing buttons.
    @pyqtSlot()
    def on_selectPushButton_clicked(self) -> None:
        id = self.getSelectedId()
        if id:
            self.done(id)

    @pyqtSlot(QTableWidgetItem)
    def on_tableWidget_itemClicked(self, item : QTableWidgetItem):
        if self.getSelectedId():
            self.selectPushButton.setEnabled(True)
        else:
            self.selectPushButton.setEnabled(False)

    @pyqtSlot(QTableWidgetItem)
    def on_tableWidget_itemDoubleClicked(self, item: QTableWidgetItem):
        self.done(self.getSelectedId())

    @pyqtSlot()
    def on_filterLineEdit_returnPressed(self) -> None:
        self.filterData()

    @pyqtSlot()
    def on_filterPushButton_clicked(self) -> None:
        self.filterData()

    @pyqtSlot()
    def on_cancelPushButton_clicked(self) -> None:
        self.close()

    @pyqtSlot(str)
    def on_filterLineEdit_textChanged(self, text:str) -> None:
        self.filterData()