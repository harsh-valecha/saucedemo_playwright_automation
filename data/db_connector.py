import os
import sqlite3

# conn = sqlite3.connect('saucedemo.db')
# cursor = conn.execute('select * from users')
# for row in cursor:
#     print(row)

def get_users():
    db_path = os.path.join(os.path.dirname(__file__), 'saucedemo.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.execute('select * from users')
    credentials = []
    for row in cursor:
        credentials.append({'username':row[1],'password':row[2]})
    conn.close()
    return credentials

print(get_users())
