"""Initial countries API example"""
import os
import json

import requests

# export COUNTRIES_API_KEY=XXXXXXXXXXXXXXXXXXXX
api_key = os.environ["COUNTRIES_API_KEY"]

# Prompt user for country and save as string variable named "search_pattern"
search_pattern = input("What country would like to search for? ")

headers = {
    'Authorization': f'Bearer {api_key}'
}

params = {
    'q': search_pattern
}

# Make the GET request to the API endpoint and store response to variable named "response"
response = requests.get(
    'https://api.restcountries.com/countries/v5',
    params=params,
    headers=headers,
    timeout=10,
)
response.raise_for_status()

# Extract the JSON (dictionaries OR list of dictionaries) from the response and store as variable named "countries_data"
countries_data = response.json()

with open("countries_response.json", "w", encoding="utf-8") as file:
    json.dump(countries_data, file, indent=2, ensure_ascii=False)
