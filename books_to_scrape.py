import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://books.toscrape.com/"
START_URL = "http://books.toscrape.com/catalogue/page-1.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_soup(url):
    res = requests.get(url, headers = headers)
    return BeautifulSoup(res.text, "html.parser")

def scrape_books():
    url = START_URL
    books = []

    while url:
        print(f"Scraping: {url}")
        soup = get_soup(url)

        articles = soup.select("article.product_pod")
        for book in articles:
            title = book.select_one("h3 a")["title"]
            price = float(book.select_one(".price_color").text.strip().replace("Â£", ""))
            availability = book.select_one(".availability").text.strip()
            rating_class = book.select_one(".star-rating")["class"]
            rating = rating_class[1]

            books.append({
                "Title": title,
                "Price (£)": price,
                "Availability": availability,
                "Rating": rating
            })

        next_btn = soup.select_one("li.next a")
        if next_btn:
            next_page = next_btn["href"]
            url = BASE_URL + "catalogue/" + next_page

        else:
            url = None
    return books

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("data/books.csv", index = False)
    print(f"Saved {len(data)} books.")


if __name__ == "__main__":
    books = scrape_books()
    save_to_csv(books)
