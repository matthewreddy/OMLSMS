import sys, os
from constants import *
import constants
import django
import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

import ui, logindlg

# enables django stuff(templates etc) to be used, make sure OMLWEB_PATH is updated to your machine in constants.py
sys.path.append(OMLWEB_PATH)
from django.conf import settings
import omlweb

import printpdf
import ctypes

def main(isTestEnviron, *argv):
    """Main function. Initializes and sets up database
    in such a way that can be used by the application.
    """

    app=QApplication(sys.argv)
    app.setOrganizationName("Oral Microbiology Laboratory")
    app.setOrganizationDomain("unc.oml.edu")
    app.setApplicationName("Oral Microbiolgy Lab Database")
    app.setWindowIcon(QIcon("icon.ico"))

    # Get an icon other than python script icon
    myappid = 'oral_micro.sterilizer_monitoring.database_client' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    #  How to get the roaming app user directory to store user info.
    #  The Dental School doesn't support roaming so this will not be used.
    #  However, I left this here for possible future use.
    #import ctypes.wintypes
    #SIDL_APPDATA = 26       # My Documents
    #SHGFP_TYPE_CURRENT = 0   # Want current, not default value
    #buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    #ctypes.windll.shell32.SHGetFolderPathW(0, CSIDL_APPDATA, 0, SHGFP_TYPE_CURRENT, buf)
    #print buf.value

    cwd = os.getcwd()
    webdir = OMLWEB_PATH.replace('\\','/') + "/omlweb"
    # Go to config.txt to see what these values are
    configValues = []
    try:
        #configValues = readConfigValues(cwd + "\\config.txt")
        configValues = readConfigValues(cwd + "\\config.txt")
    except Exception as e:
        QMessageBox.critical(None, "Error Reading Configuration File", str(e))
    else:
        # Django configure settings specifically for the application, will need to add more django if needed to these lines
        settings.configure(
            DATABASES = {
                'default': {
                    'ENGINE': 'mssql',
                    'NAME': 'omlsms',
                    'USER': '', # value is altered in logindlg
                    'PASSWORD': '', # value is altered in logindlg
                    'HOST': 'UNC-CTUCB7BC3RK', # UNC-CTUCB7BC3RK on Grayson's PC
                    'OPTIONS' : {
                                'driver' : 'ODBC Driver 17 for SQL Server',
                                },                     
                }
            },
            TEMPLATES = [ {
                 'BACKEND': 'django.template.backends.django.DjangoTemplates',
                 'DIRS': [webdir + "/account",
                        webdir + "/base",
                        webdir + "/billing",
                        webdir + "/images",
                        webdir + "/labels",
                        webdir + "/letters",
                        webdir + "/results",
                        webdir + "/reports",
                        webdir + "/summary"],
            }
        ],
            INSTALLED_APPS = (
                'omlweb',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            )
        )
        # Starts django
        django.setup()

        printpdf.pdfview_filename = configValues[PDF_VIEWER_PATH]
        printpdf.gsprint_filename = configValues[PDF_PRINTER_PATH]
        printpdf.htmltopdf_filename = configValues[HTML_CONVERTER_PATH]
        printpdf.labelPrinterName = configValues[LABEL_PRINTER]
        printpdf.defaultPrinterName = configValues[DEFAULT_PRINTER]
        printpdf.testPrinting = isTestEnviron
        constants.IMAGES_PATH = (webdir + "/images/").replace('/','\\')
        
        if len(argv):
            configValues[USER_INITIALS] = argv[0]

        # Login box initialized here
        login = logindlg.LoginDlg(configValues[DEFAULT_USER])
        if login.exec_():
            try:
                form=MainWindow(configValues, login.loginLineEdit.text(), configValues[USER_INITIALS])
                form.move(configValues[MAIN_X_POS], configValues[MAIN_Y_POS])
                form.show()
            except Exception as e:
                print(e)
                QMessageBox.critical(None, "Error Initializing Program", str(e))
            finally:
                app.exec_()


class MainWindow(QMainWindow, ui.Ui_mainWindow):
    """Overarching window that holds all dialog boxes."""

    def __init__(self, configValues, userName, defaultInitials, parent=None):
        super(MainWindow, self).__init__(parent)
        import dentistdlg, sterilizerdlg, lotdlg, renewaldlg, testdlg, reportdlg
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinMaxButtonsHint)
        self.setWindowTitle("OML Database")

        self.configValues = configValues
        self.userName = userName
        self.printer = None
        
        self.bookmark = {}
        self.currentChild = None

        self.dentistDlg = dentistdlg.DentistDlg(self)
        self.sterilizerDlg = sterilizerdlg.SterilizerDlg(self)
        self.lotDlg = lotdlg.LotDlg(self)
        self.renewalDlg = renewaldlg.RenewalDlg(self)
        self.testDlg = testdlg.TestDlg(self)
        self.reportDlg = reportdlg.ReportDlg(self)
        
        self.dialogs = [
            self.dentistDlg,
            self.sterilizerDlg,
            self.lotDlg,
            self.renewalDlg,
            self.testDlg,
            self.reportDlg
        ]

        self.userList = omlweb.models.ClientProfile.objects.all()
        self.userList = self.userList.order_by('userclass', 'last_name')
        self.director = self.userList[0]
        for number, user in enumerate(self.userList):
            self.userComboBox.insertItem(number, user.initials)
            if user.userclass == 1:
                self.director = user
            if number == 0 or user.initials == defaultInitials:
                self.user = self.userList[number]
                self.userComboBox.setCurrentIndex(number)

        # self.dentistsPushButton.clicked.connect(self.on_dentistsPushButton_clicked)
        # self.sterilizersPushButton.clicked.connect(self.on_sterilizersPushButton_clicked)
        # self.lotsPushButton.clicked.connect(self.on_lotsPushButton_clicked)
        # self.renewalsPushButton.clicked.connect(self.on_renewalsPushButton_clicked)
        # self.testsPushButton.clicked.connect(self.on_testsPushButton_clicked)
        # self.reportsPushButton.clicked.connect(self.on_reportsPushButton_clicked)
        # self.userComboBox.activated.connect(self.on_userComboBox_activated)

    
    def showMainDialog(self, show=None):
        """Defines behavior for displaying the main dialog.
        Note that only one MainDialog object should be open at once.
        In other words, you should not leave the active dialog if
        you are currently editing.
        """
        # Error where executing twice bug happens
        #print(self.dialogs, "dialogs")

        for dialog in [x for x in self.dialogs if (x.isVisible() and x.editing)]:
            print("uhoh")
            QApplication.beep()
            dialog.activateWindow()
            return
        # Hide all dialogs, saving a bookmark from the visible dialog
        for dialog in self.dialogs:
            if dialog.isVisible():
                self.bookmark.update(dialog.makeBookmark())
                dialog.hide()
        # Show the desired dialog, initialized as appropriate for the bookmark
        #print(self.bookmark, " bookmark")
        #print(show, " show")
        #print(type(show))
        if show.isHidden():
            show.move(self.pos() + QPoint(5, self.height() + 50))
            show.show(self.bookmark)
            self.currentChild = show
    
    # Functions for defining behavior upon pushing buttons.

    @pyqtSlot()
    def on_dentistsPushButton_clicked(self) -> None:
        self.showMainDialog(self.dentistDlg)
        print("dentist")
        #self.dentistsPushButton.dumpObjectInfo()
        
    @pyqtSlot()
    def on_sterilizersPushButton_clicked(self) -> None:
        self.showMainDialog(self.sterilizerDlg)

    @pyqtSlot()
    def on_lotsPushButton_clicked(self) -> None:
        self.showMainDialog(self.lotDlg)

    @pyqtSlot()
    def on_renewalsPushButton_clicked(self) -> None:
        self.showMainDialog(self.renewalDlg)

    @pyqtSlot()
    def on_testsPushButton_clicked(self) -> None:
        self.showMainDialog(self.testDlg)

    @pyqtSlot()
    def on_reportsPushButton_clicked(self) -> None:
        self.showMainDialog(self.reportDlg)
    
    @pyqtSlot(int)
    def on_userComboBox_activated(self, ind: int) -> None:
        self.user = self.userList[ind]
        if self.currentChild:
            # activate editing window again
            self.currentChild.activateWindow()

if __name__ == "__main__":
    # Run as test environment
	main(True, *sys.argv[1:])