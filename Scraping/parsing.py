import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get("https://quotes.toscrape.com")

print(response.status_code)

# Prints the full HTML
# print(response.text)

# Prints the http response code
# print(response)

htmltext = "<b> This is first comment text in HTML </b> <b> This is second comment text in HTML </b>"

# Makes a bs4 object
soup = BeautifulSoup(htmltext,'html.parser')
print(type(soup))

# Strips HTML tags and leaves just the text
comment = soup.b.text
print(comment)

# Finds the first object matching tag, returns bs4.element.Tag object
found_b = soup.find("b")
print(type(found_b))

# Finds all instances of spacified tag, returns bs4.element.ResultSet list of objects
# Can also specify extra parameters in curly braces |||soup.find_all('b', {"class":"some_class"})
found_all_b = soup.find_all('b')
print(type(found_all_b))

def printQuotes(url):
    # 1.Fetch the webpage
    response = requests.get(url)
    
    # 2. Check if request code was successful
    if response.status_code == 200:
        
         # 3.Parse with BS
         soup = BeautifulSoup(response.text, "html.parser")
        
        # 4. Extract all quotation divs        
         all_quotes = soup.find_all('div', {"class":"quote"})
         
         
         # 5. Display all quotes with for loop, filtering out only the text
         for q in all_quotes:
             quote = q.find("span", {"class":"text"})
             print(quote.text)
         
    else:
        print(f"Failed to retrieve the page. Status code: {response.status.code}")
        
printQuotes(url)
