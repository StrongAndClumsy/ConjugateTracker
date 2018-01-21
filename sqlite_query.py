import sqlite3

TRACKER_TABLES = ['tracker_benchmovement', 'tracker_squatmovement', 'tracker_upperaccessorymovement', 'tracker_loweraccessorymovement', 'tracker_deadliftmovement']
user_id = '6'
user_conn = sqlite3.connect("C:/Users/Cara/db.sqlite3")
user_cursor = user_conn.cursor()
user_name = 'katey'
user_cursor.execute("SELECT id from auth_user where username = %s " % (user_name))
for movement in TRACKER_TABLES:
    print(movement)
    conn = sqlite3.connect("C:/Users/Cara/db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT * FROM %s WHERE user_id = %s" % (movement, user_id))
    for query in cur.fetchall():
        print(query)
    conn.close()