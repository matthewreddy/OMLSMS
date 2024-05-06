"""This is a suite to run unit tests and ensure database connections and various
functions are working as they should as we go along.

Note that the SERVER, DATABASE, USERNAME and PASSWORD fields will meed to be
changed according to your database instance for some tests to pass."""

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