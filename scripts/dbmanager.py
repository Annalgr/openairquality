"""This module allows you to create and populate a Database of username and passwords."""
import sqlite3


conn = None
cursor = None

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('openaq_users.db')
    cursor = conn.cursor()
    try:
        # Check for existing table
        cursor.execute("SELECT * FROM user_database")
    except sqlite3.OperationalError:
        # Create table        
        cursor.execute('''CREATE TABLE user_database
                     (username TEXT CHAR(30) NOT NULL, 
                     password_digest TEXT CHAR(30) NOT NULL,
                     salt TEST, PRIMARY KEY (username))''')
       

