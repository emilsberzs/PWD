import sqlite3

# Connect to a database (don't forget .sqlite3 extension, otherwise extensions refuse to read it, jsyk)
connection = sqlite3.connect("items.sqlite3")

# Cursor
cursor = connection.cursor()

# Design
cursor.execute('''
                CREATE TABLE IF NOT EXISTS items(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                in_stock BOOLEAN NOT NULL,
                launch_date DATE NOT NULL)
               ''')
# SQL cheat sheet

# Creating a table

# Product database

# Commit, submits all changes made to the database
connection.commit()

# Read the table and store in variable query, 
data = cursor.execute('''
               SELECT * from items
               ''')

# Fetch all the values stored in a variable from the query
fetched_data = data.fetchall()

# Get description (not sure of what exactly yet, but will note it down anyway)
description = cursor.description
print(description)