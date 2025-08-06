import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"
response = requests.get("https://quotes.toscrape.com")

def printQuotes(url):
    # 1.Fetch the webpage
    response = requests.get(url)
    
    # 2. Check if request code was successful
    if response.status_code == 200:
        
         # 3.Parse with BS
         soup = BeautifulSoup(response.text, "html.parser")
        
        # 4. Extract all quotation divs        
         quotes = soup.find_all('div', {"class":"quote"})
         
         
         # 5. Return the list Object of quotes to the caller
         quote_data = []
        
         for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

            quote_data.append({
                'text': text,
                'author': author,
                'tags': ', '.join(tags)
            })

         return quote_data
         
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        
quotesoup = printQuotes(url)

print(quotesoup)

pd.DataFrame(quotesoup)