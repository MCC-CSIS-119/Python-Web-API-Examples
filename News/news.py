"""Demo News API script"""
import os

import requests


# export NEWS_API_TOKEN=XXX
token = os.environ["NEWS_API_TOKEN"]

params = {
    'country': 'us',
    'category': 'business',
    'apiKey': token
}

response = requests.get('https://newsapi.org/v2/top-headlines/', params=params, timeout=10)
# Is equivalent to:
response = requests.get(f'https://newsapi.org/v2/top-headlines/?country=us&category=business&apiKey={token}', timeout=10)

response.raise_for_status()
news_response = response.json()

print(f"Found {news_response['totalResults']} articles\n")

for article in news_response["articles"]:
    print(f"{article['title']}\n")
