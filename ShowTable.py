import sqlite3


def show_all():
    # Connect to database and create cursor
    conn = sqlite3.connect('disease.db')
    c = conn.cursor()
    # Query The Database
    c.execute("SELECT rowid, * FROM diseases")
    items = c.fetchall()

    for item in items:
        print(item)
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


show_all()
