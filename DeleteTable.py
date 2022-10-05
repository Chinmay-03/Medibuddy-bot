import sqlite3

conn = sqlite3.connect('disease.db')

c = conn.cursor()

c.execute("DROP TABLE diseases")

conn.commit()
conn.close()

print("Table has been deleted.")