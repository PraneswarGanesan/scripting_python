import requests
from bs4 import BeautifulSoup


def scrap_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = []
    for headline in soup.find_all('h2'):
        headlines.append(headline.text)

    return headlines


url = 'https://www.bbc.com/news'
headlines = scrap_headlines(url)
for headline in headlines:
    print(headline)