import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com/news'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the headlines (assuming they are in <h2> tags)
    headlines = soup.find_all('h2')

    # Print each headline
    for headline in headlines:
        print(headline.text)
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
