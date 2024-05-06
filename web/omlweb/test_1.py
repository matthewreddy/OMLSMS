"""This is a suite to run unit tests and ensure database connections and various
functions are working as they should as we go along.

Note that the SERVER, DATABASE, USERNAME and PASSWORD fields will meed to be
changed according to your database instance for some tests to pass.

Note that some functions are redefined here in order to test some functions without altering settings
(There were issues with the path that, if not resolved, will cause 0 tests to run, so this ensures
anybody can at least run tests with just a server)"""

import pyodbc
import pytest

SERVER = 'UNC-PF2A3Z3S'            # put your SQL server instance here
DATABASE = 'omlsms'                # put the name of the SQL database here
USERNAME = 'UNC-PF2A3Z3S\Connor'   # add the username here
PASSWORD = ''                      # if needed, add the password here
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};encrypt=no;Trusted_Connection=yes;'


# Attempt to make a connection to the database
def make_connection():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        assert cursor.fetchone() is not None, "Basic query not executed, possibly no connection"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()

# Test the database connection to ensure it is recognized
def test_connection():
    make_connection()


# Pull the value of the Director from the query
def pull_director():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.client_user")
        roles = cursor.fetchall()
        assert roles[0][4] == "Director"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()

# Test the value of the Director from the query
def test_director():
    pull_director()


# Pull the value of the Lab Manager from the query
def pull_manager():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.client_user")
        roles = cursor.fetchall()
        assert roles[2][4] == "Lab Manager"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()
    
# Test the value of the Lab Manager from the query
def test_manager():
    pull_manager()


# Pull the value of the Lab Tech from the query
def pull_lab_tech():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.client_user")
        roles = cursor.fetchall()
        assert roles[3][4] == "Lab Tech"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()

# Test the value of the Lab Tech from the query
def test_lab_tech():
    pull_lab_tech()


# Pull the value of the Accounts Manager from the query
def pull_accounts_manager():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.client_user")
        roles = cursor.fetchall()
        assert roles[4][4] == "Accounts Manager"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()


# Test the value of the Accounts Manager from the query
def test_accounts_manager():
    pull_accounts_manager()

def pull_dentist():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.sms_dentist")
        roles = cursor.fetchall()
        assert roles[1][1] == "Reynolds Mountain Dentistry"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()

# Test the value of a dentist from the query
def test_dentist():
    pull_dentist()


def pull_sterilizer():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.sms_sterilizer")
        roles = cursor.fetchall()
        assert roles[2][7] == "2101B10104"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()

# Test the value of a dentist from the query
def test_sterilizer():
    pull_sterilizer()


def pull_renewal():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.sms_renewal")
        roles = cursor.fetchall()
        assert roles[7][2] == "R315731"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()

# Test the value of a renewal from the query
def test_renewal():
    pull_renewal()


def pull_lot():
    conn = pyodbc.connect(connectionString)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.sms_lot")
        roles = cursor.fetchall()
        assert roles[6][1] == "GS106E"
    except pyodbc.Error as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        conn.close()
        

# Test the value of a lot from the query
def test_lot():
    pull_lot()

def encodeTo128Font(value): # from db_rewrite.djprint
    if value == 0:
        return 128
    elif value >= 95:
        return value + 50
    else:
        return value + 32

def test_encoding_1():
    assert encodeTo128Font(0) == 128

def test_encoding_2():
    assert encodeTo128Font(95) == 145

def test_encoding_3():
    assert encodeTo128Font(94) == 126

def chunker(seq, size):            # from db_rewrite.djprint
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def encodeToCode128(id):            # from db_rewrite.djprint
    """Encode ID string to condensed Code 128c
    (Start C) (Encoded Pairs) (Checksum) (End Char)
    checksum =  Value of Start C + (Value * Position) of Encoded Pairs
    """
    checksum = 105
    code = ""
    for position, pair in enumerate(chunker(id, 2)):
        checksum += int(pair) * (position + 1)
        code = code + "&#%d" % encodeTo128Font(int(pair))
    checksum = encodeTo128Font(checksum % 103)
    return "&#155" + code + ("&#%d" % checksum) + "&#156"

# testing some manually calculated encodings below to ensure encodeToCode128 outputs correctly
def test_encoding_4():
    assert encodeToCode128('123456') == "&#155&#44&#66&#88&#76&#156"

def test_encoding_5():
    assert encodeToCode128('1427') == "&#155&#46&#59&#102&#156"

def test_encoding_6():
    assert encodeToCode128('274705') == "&#155&#59&#79&#37&#67&#156"
