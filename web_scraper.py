import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)

        quotes.append({
            "quote": text,
            "author": author
        })

    # Display results
    print("===== Scraped Quotes =====")

    for item in quotes:
        print("\nQuote:", item["quote"])
        print("Author:", item["author"])

    # Save as JSON
    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(quotes, file, indent=4, ensure_ascii=False)

    # Save as text
    with open("quotes.txt", "w", encoding="utf-8") as file:
        for item in quotes:
            file.write(item["quote"] + " - " + item["author"] + "\n")

    print("\nData saved successfully!")
    print("Created: quotes.json and quotes.txt")

except requests.RequestException as e:
    print("Error while accessing website:", e)