import mysql.connector
import json


def connect_to_db():
    """Connect to database"""
    with open("credentials.json") as f:
        creds = json.loads(f.read())
    db = mysql.connector.connect(host=creds["database"]["host_name"],
                                 user=creds["database"]["user_name"],
                                 passwd=creds["database"]["pass"],
                                 database=creds["database"]["db_name"])
    cursor = db.cursor()
    return cursor
