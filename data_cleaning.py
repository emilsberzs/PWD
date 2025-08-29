import pandas as pd
import numpy as np

# Store the csv data in a DataFrame
df = pd.read_csv('practice.csv')

# TODO 
# -Extract Values
# -Format data types
# -Check data types
# -Proceed to next column

### Extract values
# Map specific column in dataframe:

def concatenate(title):
    return title + '10'

# Split on colon and return first element (second index) of return list 
# stripped of whitespace
def extract_title(string):
    return string.split(':')[1].strip()
    
# Extract and clean title, then store back to dataframe. Then instock, review.
df['name'] = df['name'].map(extract_title)
df['instock'] = df['instock'].map(extract_title)
df['review'] = df['review'].map(extract_title)
df['launch_date'] = df['launch_date'].map(extract_title)

# 

# Extract and clean up the price
def extract_price(string):
    price = string.split(':')[1].strip()
    if price == '':
        return np.nan
    else: 
        return price.split('£')[1].strip()

# Map cleaned up price to exisitng values and store back into the dataframe
# Keep in mind that price is currently a string (shows as an object to me)
df['price'] = df['price'].map(extract_price)
print(df['price'].describe)

# And now map the price string to a float
df['price'] = df['price'].map(float)
print(df['price'].describe)


# Count rating stars, using 'string'.count('countwhat')
def count_stars(rating):
    return rating.count('★')

df['rating'] = df['rating'].map(count_stars)
print(df)

print(df.dtypes)

# Cleanup launchdate converting to standart datetime
def date_cleanup(date):
    return pd.to_datetime(date, errors='coerce').date()

df['launch_date'] = df['launch_date'].map(date_cleanup)
print('\nAFTER launch_date CLEANUP\n')
print(df)


# Remove duplicates from dates column
df= df.drop_duplicates(subset='name', keep='first')
print('\nAFTER REMOVING DUPLICATES:\n')
print(df)



# Store the corrected dataframe back to a csv file
df.to_csv('practice_corrected.csv', index = False)