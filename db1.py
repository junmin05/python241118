import sqlite3

# create database on workspace
conn = sqlite3.connect('test.db')

# create cursor
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE if not exists PhoneBook (
    Name text,
    PhoneNum text
)""")

# insert data
cursor.execute("INSERT INTO PhoneBook VALUES('derick', '010-1234-5678')")

name = 'freeman'
phoneNumber = '010-7777-7777'
cursor.execute("INSERT INTO PhoneBook VALUES(?, ?)", (name, phoneNumber))

# run several sql queries
datalist = [('freeman', '010-9999-9999'), ('john', '010-8888-8888')]
cursor.executemany("INSERT INTO PhoneBook VALUES(?, ?)", datalist)

# search data
cursor.execute("SELECT * FROM PhoneBook")
print(cursor.fetchall())

