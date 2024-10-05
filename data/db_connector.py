import os
import sqlite3

# conn = sqlite3.connect('saucedemo.db')
# cursor = conn.execute('select * from users')
# for row in cursor:
#     print(row)

def get_valid_users():
    db_path = os.path.join(os.path.dirname(__file__), 'saucedemo.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('select * from users where user_type = "valid"')
    credentials = []
    for row in cursor:
        credentials.append({'username':row[1],'password':row[2]})
    conn.close()
    return credentials

# print(get_valid_users())

def get_invalid_users():
    db_path = os.path.join(os.path.dirname(__file__), 'saucedemo.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('select * from users where user_type = "invalid"')
    credentials = []
    for row in cursor:
        credentials.append({'username':row[1],'password':row[2]})
    conn.close()
    return credentials

# print(get_invalid_users())

def execute_query(query):
    db_path = os.path.join(os.path.dirname(__file__), 'saucedemo.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(query)
    results = []
    for row in cursor:
        results.append(row)
    return results

print(execute_query('select * from users where used = 0 and user_type ="valid" order by id limit 1'))
