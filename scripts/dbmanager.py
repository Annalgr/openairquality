"""
This module allows to create and populate a SQL database
of usernames and passwords.
"""

import sqlite3
import hashlib
import argparse
import random
import os

conn = None
cursor = None


def open_and_create():
    """Check for existing sql db or create a new one with
       a data schema to store: username, password and salt,
       using username as primary key.
    """
    global conn
    global cursor
    os.chdir("../pypackage")
    conn = sqlite3.connect('openaq_users.db')
    cursor = conn.cursor()
    try:
        # Check for existing table
        cursor.execute("SELECT * FROM user_database")
    except sqlite3.OperationalError:
        # Create table if not exists
        cursor.execute('''CREATE TABLE user_database
                     (username CHAR(30) NOT NULL,
                     password_digest CHAR(64) NOT NULL,
                     salt CHAR(30), PRIMARY KEY (username))''')


def parse_args():
    """Parse user inputs: username and password."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a username (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a username and password"
                                   "(requires -p)", required=False)
    return parser.parse_args()


def save_new_username(username, password):
    """Save new user in the db if its username is not already present.

       Key arguments:
       username -- string name to add in db
       password -- string to add as password in db
    """
    global conn
    global cursor

    # Check the username can fit the database
    if len(username) > 30:
        print("Username too long. Plese, use less than 30 chars.")
        return

    # Check the username is not already existing
    u_row = cursor.execute(
        "SELECT * FROM user_database WHERE username = ?", (username,)
    )
    existing_u = u_row.fetchall()
    if existing_u:
        words = ['Unicorn', 'Farmer', '1998', 'Thunberg']
        print("Username already existing. Please, select another one."
              "\nYou can try with:")
        for i in words:
            print(username + i)

    else:
        salt = str(random.random())
        digest = salt + password
        for i in range(1000):
            digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
        cursor.execute("INSERT OR REPLACE INTO user_database VALUES (?,?,?)",
                       (username, digest, salt))
        print("The registration has been successful")
        conn.commit()


def check_for_username(username, password):
    """Check for existing user for log-in.

       Key arguments:
       username -- string name to be selected from the db
       password -- string to authenticate the user
    """
    global conn
    global cursor
    row = cursor.execute(
        "SELECT * FROM user_database WHERE username = ?", (username,)
    )
    results = row.fetchall()
    salt = str(results[0][2])
    digest = salt + password
    for i in range(1000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    if digest == results[0][1]:
        print('Successful log-in.')
    else:
        print("User is not present, or password is invalid")
    conn.commit()


if __name__ == "__main__":
    args = parse_args()
    open_and_create()
    if args.a and args.p:
        save_new_username(args.a, args.p)
    elif args.c and args.p:
        check_for_username(args.c, args.p)
    conn.close()
