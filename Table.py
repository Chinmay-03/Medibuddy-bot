import sqlite3

conn = sqlite3.connect('disease.db')

c = conn.cursor()
c.execute('''CREATE TABLE diseases (
    disease text,
    symptoms text,
    causes text,
    cure text
        )''')

conn.commit()
conn.close()

print("Table has been created!")