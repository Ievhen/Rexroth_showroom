import mysql.connector


def db_connect(ip, username, password, db):
    return mysql.connector.connect(
        host=ip,
        user=username,
        password=password,
        database=db
    )


# returns the sql request result
def execute_request(db, req):
    cursor = db.cursor()
    cursor.execute(req)
    return cursor.fetchall()


# send request to database and don't return nothing, needed for UPDATE and INSERT operations
def update_request(db, req):
    cursor = db.cursor()
    cursor.execute(req)


def request(command, column, table, where_arg=None):
    if where_arg is not None:
        return f'{command} {column} FROM {table} WHERE {where_arg}'
    else:
        return f'{command} {column} FROM {table}'


def insert_request(table, column, value, where_arg):
    return f'INSERT INTO {table}({column}) VALUES({value} WHERE {where_arg})'


def close(db):
    db.close()
