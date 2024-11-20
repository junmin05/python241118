import sqlite3

# create database on workspace
conn = sqlite3.connect(r"C:\workspace\sample2.db")

# create cursor
cursor = conn.cursor()

# search data
cursor.execute("SELECT * FROM Employee")
print(cursor.fetchall())

# # commit
# conn.commit()

