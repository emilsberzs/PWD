import pandas as pd
import sqlite3

connection = sqlite3.connect('items.sqlite3')
cursor = connection.cursor()

# Python/SQL way
row = cursor.execute("SELECT * FROM items")
all_rows = row.fetchall()
print(all_rows)

# Pandas way
QUERY = "SELECT * FROM items"

# Read data into pd dataframe
df = pd.read_sql_query(QUERY, connection)
print(df)

# Explore type
print(df.dtypes)
# Or 
print(type(df['name'][0]))
print(type(df['launch_date'][0]))

### Updating database

 # Change in_stock of 'Product A' to 0
df.loc[df["name"] == "Product A", "in_stock"] = 1
print(df)

 # Write change back to SQL
df.to_sql("items", connection, if_exists="replace", index=False)

 # Drop a column (default axis is rows, so to drop column we need to specify additional argument axis=1, and also inplace=True (not sure whats that for tho))
df.drop("in_stock", axis=1, inplace=True)
print("\nAFTER DROPPING in_stock\n")
print(df['launch_date'])
# Now we could do df.to_sql("items, connection, if_exists='replace', index = False") to commit, but i won't

