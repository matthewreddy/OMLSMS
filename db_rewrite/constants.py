"""This file defines constants that are used throughout the application."""

import datetime, locale, sys

#locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )
locale.setlocale( locale.LC_ALL, '' )

# Configuration File Constants
CONFIG_FILENAME = "\OMLSMS\config.txt"
# This is right on Grayson's PC CONFIG_FILENAME = "\\OMLSMS\\config.txt"
#must be set here for imports
#OMLWEB_PATH = "C:\\Users\\gray1\\comp523\\web" #test directory, change to whatever your path is
#OMLWEB_PATH = "C:\\Users\\Grayson\\omlsms\\web" #installation directory
OMLWEB_PATH = "C:\\Users\\Connor\\Desktop\\School Stuff\\Grad School\\Work\\OMLSMS\\web"
#OMLWEB_PATH = "J:\\Share\\D R C\\OML\\new-omlsms-db\\web"
IMAGES_PATH = "" #set by configuration file

# Defines a range of dates that should be in the database
# This does not need to be updated unless this range is no longer covered
DATABASE_START_DATE = datetime.date(year = 1990, month=1, day=1)
DATABASE_STOP_DATE = datetime.date(year = 2050, month=1, day=1)

# Database File Constants
DENTIST_ID_WIDTH = 5
STERILIZER_ID_WIDTH = 7
RENEWAL_ID_WIDTH = 10
LOT_ID_WIDTH = 3
#TEST_ID_WIDTH = 9   # I'm not sure what this is for.
TEST_ID_WIDTH = 12
STRIP_ID_WIDTH = 2

# Policy settings
DAYS_UNTIL_OVERDUE = 30
COMPLIANT_TESTS_PER_YEAR = 42
REPORT_HISTORY_EXTRA_DAYS = 14
REPORT_HISTORY_DEFAULT_DAYS = 1000
MAX_LATE_FEE = 100
MAX_DAYS_FOR_COLLECTIONS = 730
DAYS_FOR_TEST = 7
MAX_DAYS_FOR_TEST_ENTRY = 60

# Display settings
MAX_FIND_DISPLAY_ROWS = 10000

# Default values for new records
DEFAULT_NUM_TESTS = 26
DEFAULT_RENEWAL_TEST = 22
DEFAULT_RENEWAL_FEE = 155.00
DEFAULT_STERILIZER_METHOD = 1   # 1 = Steam
DEFAULT_LOT_COUNT = 10000
DEFAULT_CHEMICAL_VAPOR = 3   # 3 = Ignore

# Text File Configuration
NUM_CONFIG_VALUES = 12
[
    USER_INITIALS,
    DEFAULT_USER,
    SERVER_ADDRESS,
    SERVER_PORT,
    DATABASE_NAME,
    MAIN_X_POS,
    MAIN_Y_POS,
    PDF_VIEWER_PATH,
    PDF_PRINTER_PATH,
    HTML_CONVERTER_PATH,
    #IMAGES_PATH,
    LABEL_PRINTER,
    DEFAULT_PRINTER,
] = range(NUM_CONFIG_VALUES)

def readConfigValues(filename):
    """Parses configuration values from a file and returns them in a Python list."""
    configValues = []
    configFile = open(filename,"r")
    for line in configFile:
        value = line.split('#')[0].strip()
        if value != "":
            configValues.append(value)
    assert len(configValues) == NUM_CONFIG_VALUES
    if configValues[SERVER_PORT] == 'default':
        configValues[SERVER_PORT] = ''
    else:
        configValues[SERVER_PORT] = int(configValues[SERVER_PORT])
    configValues[MAIN_X_POS] = int(configValues[MAIN_X_POS])
    configValues[MAIN_Y_POS] = int(configValues[MAIN_Y_POS])
    return configValues

#
# Date formating and conversions
#
DATETIME_FORMAT = "%m/%d/%Y"
SHORT_DATETIME_FORMAT = "%m/%d/%y"

def RecordDateToText(value, shortened=False):
    """Allows for converting a record date (datetime object) into a string."""
    return value.strftime(SHORT_DATETIME_FORMAT if shortened else DATETIME_FORMAT) \
        if value else ""
   
def FormDateToRecord(value, shortened=False):
    """Allows for converting a string into a record date (datetime object)."""
    return datetime.datetime.strptime(
        str(value), SHORT_DATETIME_FORMAT if shortened else DATETIME_FORMAT
    ).date() if value else None

def DateRangeForMonth(year, month):
    """Provides a range for a specific year/month pair, specifically the
    first day of the month, then the first day of the next month.
    For example, DateRangeForMonth(2000, 3) will return two datetime
    objects: one for 03/01/2000, and one for 04/01/2000.
    """
    start = datetime.date(year, month, 1)
    stop = datetime.date(
        year if month < 12 else year + 1,
        month + 1 if month < 12 else 1,
        1
    )
    return start, stop

#
# Currency formating
#
def NumToCurrency(value):
    """Converts a numeric value into currency."""
    try:
        return locale.currency(float(value), grouping=True)
    except:
        return ""

def CurrencyToNum(value):
    """Converts a currency value into a float number."""
    try:
        return float(value.translate(None, "$,"))
    except:
        return None

def GetSterilizerIDRange(dentist_id):
    """Returns a sterilizer ID range for a specific dentist by their ID."""
    w = STERILIZER_ID_WIDTH - DENTIST_ID_WIDTH
    start = dentist_id * (10 ** w)
    stop = ((dentist_id + 1) * (10 ** w)) - 1
    return (start, stop)

def SterilizerToRenewalIDRange(sterilizer_id):
    """Returns a renewal ID range for a specific sterilizer by its ID."""
    w = RENEWAL_ID_WIDTH - STERILIZER_ID_WIDTH
    start = sterilizer_id * (10 ** w)
    stop = ((sterilizer_id + 1) * (10 ** w)) - 1
    return (start, stop)

def SterilizerToDentistID(sterilizer_id):
    """Returns the dentist ID corresponding to a specific sterilizer by its ID."""
    return int(str(sterilizer_id).zfill(STERILIZER_ID_WIDTH)[0:DENTIST_ID_WIDTH])

def RenewalToDentistID(renewal_id):
    """Returns the dentist ID corresponding to a specific renewal by its ID."""
    return int(str(renewal_id).zfill(RENEWAL_ID_WIDTH)[0:DENTIST_ID_WIDTH])

def RenewalToSterilizerID(renewal_id):
    """Returns the sterilizer ID corresponding to a specific renewal by its ID."""
    return int(str(renewal_id).zfill(RENEWAL_ID_WIDTH)[0:STERILIZER_ID_WIDTH])

def RenewalToLotID(renewal_id):
    """Returns the lot ID corresponding to a specific renewal by its ID."""
    return int(str(renewal_id).zfill(RENEWAL_ID_WIDTH)[STERILIZER_ID_WIDTH:])

def ZeroNone(value):
    """Validates a value by putting 0 in its place if it is None.
    Typically used for numeric variables.
    """
    if value:
        return value
    else:
        return 0
    
def NullNone(value):
    """Validates a value by putting an empty string in its place if it is None.
    Typically used for string variables.
    """
    if value:
        return value
    else:
        return ""
