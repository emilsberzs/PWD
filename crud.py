"""
SELECT
SQL: SELECT column_name FROM table_name;
Pandas: df['column_name']
Usage: In Pandas, you can select a specific column by simply referencing the column name within the DataFramedf. If you want to select multiple columns, you can use:

WHERE
SQL: SELECT * FROM table_name WHERE condition;
Pandas: df[df['column_name'] == value]
Usage: In Pandas, you can filter rows by using Boolean indexing. If you want to filter rows based on a condition in a column, you can use:

GROUP BY
SQL: SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;
Pandas: df.groupby('column_name').size()
Usage: In Pandas, the groupby() function is used to group data by one or more columns. After grouping, you can perform aggregation operations, such as counting the number of rows in each group.
"""

import sqlite3

# Connect to a database (don't forget .sqlite3 extension, otherwise extensions refuse to read it, jsyk)
connection = sqlite3.connect("items.sqlite3")

# Cursor
cursor = connection.cursor()

# Design the table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS items(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                in_stock BOOLEAN NOT NULL,
                launch_date DATE NOT NULL)
               ''')

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
print("PRINT DESCRIPTION")
print(description)

# Insert values into the items table. If we skip id in the INSERT query, and somehow query runs multiple times, it will create duplicates.
# Also if running dupicate query with same id for insertion, will produce UNIQUE constraint error
cursor.execute('''
               INSERT OR IGNORE INTO items (id, name, price, in_stock, launch_date) VALUES
               ("1", "Product A", 29.00, 1, "02-01-2025"),
               ("3", "Product B", 39.00, 0, "05-01-2025"),
               ("4", "Product B", 19.00, 1, "02-08-2025"),
               ("2", "Product X", 9.00, 1, "02-08-2024")
               ''')

# And commmit the changes to the database
connection.commit()

# Query the products table
row = cursor.execute("SELECT * FROM items")
values = row.fetchall()
print("\nVALUES:")
print(values)

def print_table(cursor):
    row = cursor.execute("SELECT * FROM items")
    values = row.fetchall()
    
    for value in values:
        print(value)

print('\nFIRST PRINT WITH print_table\n')
print_table(cursor)
print('\n')


# Select launch date and name from items
date_and_name = cursor.execute("SELECT launch_date, name from items")
print("SELECT launch_date, name from items:\n")
print(date_and_name.fetchall())


# Select and where
in_stock_items = cursor.execute("SELECT  * from items WHERE in_stock==TRUE")
print("\nSELECT  * from items WHERE in_stock==TRUE\n")
print(in_stock_items.fetchall())

# Update values in table
cursor.execute("UPDATE items SET price=99.99, in_stock=0 WHERE name =='Product A'")   
print("\nUPDATE items SET price=99.99, in_stock=0 WHERE name =='Product A'\n")          
print_table(cursor)

# Rename the table
#cursor.execute("ALTER TABLE items RENAME TO new_items")
#cursor.execute("ALTER TABLE new_items RENAME TO items")
print("\nAFTER RENAMES:")
print_table(cursor)

# Delete product from table
#cursor.execute("DELETE FROM items WHERE name == 'Product A'")
print('\nAFTER DELETING PRODUCT A')
print_table(cursor)

# Drop the table
# cursor.execute("DROP TABLE items")
print("\nDESCRIPTION AFTER DROPPING THE TABLE\n")
print(cursor.description)

# Commit all the changes
connection.commit()
print_table(cursor)