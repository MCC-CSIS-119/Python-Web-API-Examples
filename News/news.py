"""Demo News API script"""
import os

import requests


# export NEWS_API_TOKEN=XXX
token = os.environ["NEWS_API_TOKEN"]

params = {
    'country': 'us',
    'category': 'business',
    'apiKey': token,
    'pageSize': 100 # Increasing to max size 100 (default is 20)
}

response = requests.get('https://newsapi.org/v2/top-headlines/', params=params, timeout=10)
# This is equivalent to requests.get(f'https://newsapi.org/v2/top-headlines/?country=us&category=business&apiKey={token}')

response.raise_for_status()
news_response = response.json()

print(f"Found {news_response['totalResults']} articles\n")

count = 1
for article in news_response["articles"]:
    print(f"{count}. {article['title']}\n")
    count += 1
