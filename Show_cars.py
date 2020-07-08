import sqlite3

conn = sqlite3.connect("list_of_cars.db")
cursor = conn.cursor()
cursor.execute('''SELECT * FROM list_of_refs''')

row = cursor.fetchall()
data_base = [x[0] for x in row]

for x in data_base:
    print(x)