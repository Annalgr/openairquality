"""Check the user is allowed to run the code."""

import sqlite3
import hashlib
import os


def check_db(args):
    """Check if the user is registered in the database.

       Connect to the sqlite3 database. If the user is registered verify
       whether its password is correct adding the salt and computing the
       hash, otherwise return helpful message to the user.

       Key arguments:
       args -- argparse user inputs (username and password)
    """
    # Open connection to the registered users db
    base_path = "pypackage"
    users_db = "openaq_users.db"
    conn = sqlite3.connect(os.path.join(base_path, users_db))
    cursor = conn.cursor()

    # Check for username
    row = cursor.execute("SELECT * FROM user_database WHERE username = ?",
                         (args.username,))
    results = row.fetchall()
    conn.commit()

    if results:
        # Add salt
        salt = str(results[0][2])
        digest = salt + args.password

        # Compute the hash
        for i in range(1000):
            digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()

        # Check for password
        if digest == results[0][1]:
            print('Successful log-in. Welcome {}!'.format(args.username))
            return True

        else:
            print(
                "Password is invalid for user {}.".format(args.username)
            )
            return False
    else:
        print("Username not present.")
        return False
