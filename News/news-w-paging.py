"""Demo News API script"""
import os

import requests
# import pprint


# export NEWS_API_TOKEN=XXX
token = os.environ["NEWS_API_TOKEN"]

page = 1
max_pages = 1 # Max pages to return

while page <= max_pages:
    params = {
        'country': 'us',
        'category': 'business',
        'apiKey': token,
        'page': page
    }

    response = requests.get('https://newsapi.org/v2/top-headlines/', params=params, timeout=10)
    response.raise_for_status()

    news_response = response.json()

    print(f"Page {page}: Found {news_response['totalResults']} articles\n")

    for article in news_response["articles"]:
        print(f"{article['title']}\n")

    # pprint.pprint(news_response)

    page += 1
