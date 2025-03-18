import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "http://quotes.toscrape.com"

# Step 1: Make an HTTP request to get the page content
response = requests.get(url)

# Step 2: Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully retrieved the page!")
   
    # Step 3: Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
   
    # Step 4: Find all quotes and authors
    quotes = soup.find_all('span', class_='text')  # The quote text is inside <span> with class 'text'
    authors = soup.find_all('small', class_='author')  # The author name is inside <small> with class 'author'
   
    # Step 5: Loop through quotes and authors and print them
    for quote, author in zip(quotes, authors):
        print(f"Quote: {quote.text}")
        print(f"Author: {author.text}")
        print('-' * 40)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
  
