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

# Insert values into the items table. If we skip id in the INSERT query, and somehow query runs multiple times, it will create duplicates.
# Also if running dupicate query with same id for insertion, will produce UNIQUE constraint error
# cursor.execute('''
#                INSERT INTO items (id, name, price, in_stock, launch_date) VALUES
#                ("1", "Product A", 29.00, 1, "02-01-2025"),
#                ("3", "Product B", 39.00, 0, "05-01-2025"),
#                ("4", "Product B", 19.00, 1, "02-08-2025"),
#                ("2", "Product X", 9.00, 1, "02-08-2024")
#                ''')

# And commmit the changes to the database
connection.commit()

# Query the products table
# row = cursor.execute("SELECT * FROM items")
# values = row.fetchall()
# print(values)

def print_table(cursor):
    row = cursor.execute("SELECT * FROM items")
    values = row.fetchall()
    
    for value in values:
        print(value)

print_table(cursor)


# Select launch date and name from items
date_and_name = cursor.execute('''
               SELECT launch_date, name from items
               ''')
print(date_and_name.fetchall())


# Select and where
in_stock_items = cursor.execute('''
               SELECT  * from items WHERE in_stock==TRUE
               ''')
print(in_stock_items.fetchall())

# Update values in table
cursor.execute('''
               UPDATE items SET price=99.99, in_stock=0 WHERE name =='Product A'
               ''')
print_table(cursor)