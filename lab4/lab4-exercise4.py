#!/usr/bin/env python3
import sqlite3

id = 4
temperature = 0.0
date = '2014-01-05'

dbconnect = sqlite3.connect("michaeldb.db")
dbconnect.row_factory = sqlite3.Row

cursor = dbconnect.cursor()
for i in range(10):
    id += 1
    temperature += 1.1
    cursor.execute('''insert into temperature values (?, ?, ?)''', (id, temperature, date))

dbconnect.commit()
cursor.execute('SELECT * FROM temperature')

for row in cursor:
    print(row['id'],row['temp'],row['date'])

cursor.execute('''insert into kitchen values (1, 'door', 'kitchen')''')
cursor.execute('''insert into kitchen values (2, 'temperatue', 'kitchen')''')
cursor.execute('''insert into kitchen values (3, 'door', 'garage')''')
cursor.execute('''insert into kitchen values (4, 'motion', 'garage')''')
cursor.execute('''insert into kitchen values (5, 'temperature', 'garage')''')

dbconnect.commit()
cursor.execute('SELECT * FROM kitchen WHERE zone="kitchen"')

for row in cursor:
    print(row['sensorID'],row['type'],row['zone'])

cursor.execute('SELECT * FROM kitchen WHERE type="door"')

for row in cursor:
    print(row['sensorID'],row['type'],row['zone'])
dbconnect.close()
