import sqlite3
conn = sqlite3.connect('uniqueconstrain.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE users ( user_id INTEGER PRIMARY KEY, user_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE); ''')
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (1, 'Tony Stark', 'Tony.stark@example.com');''')
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (2, 'Brad Pitt', 'Brad.pitt@example.com');''')

cursor.execute('''select *from users;''')
print(cursor.fetchall())

# Trying to insert a user with the same email (Error Conditions)
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (3, 'nosfaretu dec', 'nosfaretu.dec@example.com');''')  

conn.commit()
conn.close()