import sqlite3

# conn = sqlite3.connect('saucedemo.db')
# cursor = conn.execute('select * from users')
# for row in cursor:
#     print(row)

def get_users():
    conn = sqlite3.connect('saucedemo.db')
    cursor = conn.execute('select * from users')
    credentials = []
    for row in cursor:
        credentials.append({'username':row[1],'password':row[2]})
    conn.close()
    return credentials

# print(get_users())
