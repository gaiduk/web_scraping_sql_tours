import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


# Query all data based on the condition
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
# cursor.execute("SELECT * FROM events WHERE band='Lions'")
rows = cursor.fetchall()
print(rows)

# Query columns
cursor.execute("SELECT band, city FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)


# Insert new rows
# new_rows = [('Cats', 'Cat City', '2088.10.18'),
#             ('Hens', 'Hens City', '2088.10.18')]\
#
# cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_rows)
# connection.commit()

