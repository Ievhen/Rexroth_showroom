import mysql.connector


def db_connect(localhost, username, password, db):
    return mysql.connector.connect(
        host=localhost,
        user=username,
        password=password,
        database=db
    )
