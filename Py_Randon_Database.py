import sqlite3
import random

#Connect to the databatestingse or create a new one
conn = sqlite3.connect('Testing7.db') #Change the name of the database to what is desired

#Create a cursor object
cursor = conn.cursor()

#Creates a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS random_values (
        id INTEGER PRIMARY KEY,
        value INTEGER
    )
''')

#Generate and insert random values into the table
values = []
for i in range(10000):  # Adjust for desired number of values
    value = random.randint(1, 100)  # Generate a random value between 1 and 100
    values.append((i+1, value))

cursor.executemany('INSERT INTO random_values (id, value) VALUES (?, ?)', values)

#Close the database connection
conn.close()
