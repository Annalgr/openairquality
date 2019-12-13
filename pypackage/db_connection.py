"""Check the user is allowed to run the code."""

import sqlite3
import hashlib


def check_db(args):
    # Open connection to the registered users db
    conn = sqlite3.connect('pypackage/openaq_users.db')
    cursor = conn.cursor()

    # Check for username
    row = cursor.execute("SELECT * FROM user_database WHERE username = ?",
                         (args.username,))
    results = row.fetchall()
    conn.commit()

    if results:
        # Add salt
        salt = str(results[0][2])
        concat = salt + args.password

        # Compute the hash
        for i in range(1000):
            digest = hashlib.sha256(concat.encode('utf-8')).hexdigest()

        # Check for password
        if digest == results[0][1]:
            print('Successful log-in. Welcome {}!'.format(args.username))
            return True

        else:
            return print(
                "Password is invalid for user {}.".format(args.username)
            )
    else:
        return print("Username not present.")
