import requests
from bs4 import BeautifulSoup


def scrape_amazon_books(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all book elements on the page
        books = soup.find_all('div', {'class': 's-result-item'})

        # Iterate through each book element
        for book in books:
            # Extract book title
            title = book.find('h2').text.strip()

            # Extract book author(s)
            author = book.find('span', {'class': 'a-size-base'}).text.strip()

            # Extract book price
            price = book.find('span', {'class': 'a-price-whole'}).text.strip()

            # Extract book rating
            rating = book.find('span', {'class': 'a-icon-alt'}).text.strip()

            # Print the scraped data
            print("Title:", title)
            print("Author:", author)
            print("Price:", price)
            print("Rating:", rating)
            print("--------------------")
    else:
        print("Failed to retrieve page.")


url = "https://www.amazon.com/s?k=python+programming+books"
scrape_amazon_books(url)

