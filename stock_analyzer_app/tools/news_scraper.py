import requests
from bs4 import BeautifulSoup

def get_latest_news(company_name):
    query = company_name + " stock news"
    url = f"https://www.google.com/search?q={query}&tbm=nws"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    articles = soup.select("div.dbsr")

    news_items = []
    for article in articles[:5]:
        title = article.select_one("div.JheGif.nDgy9d").text
        link = article.a["href"]
        news_items.append(f"{title} - {link}")
    return news_items