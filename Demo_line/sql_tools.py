import mysql.connector


def db_connect(ip, username, password, db):
    return mysql.connector.connect(
        host=ip,
        user=username,
        password=password,
        database=db
    )


def execute_request(db, request):
    cursor = db.cursor()
    cursor.execute(request)
    return cursor.fetchall()


def request(command, column, table, where_arg=None):
    if where_arg is not None:
        return f'{command} {column} FROM {table} WHERE {where_arg}'
    else:
        return f'{command} {column} FROM {table}'
