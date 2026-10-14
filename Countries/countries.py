"""Initial countries API example"""
import os
import pprint

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

# Developer only (do not print this in your final code): Print the type of object "countries_data" is
#  This will help guide your next steps. Is it a list? Is it a dictionary?
print(f"The response is of type: {type(countries_data)}\n")

# Developer only (do not print this in your final code): Pretty print the type of object "countries_data" is. This should help you understand 
# the structure of the object you're dealing with
print("Pretty printing countries_data:\n")
pprint.pp(countries_data)

# # The API wraps matched countries in data.objects.
# countries = countries_data['data']['objects']

# print(f"Found {len(countries)} countries\n")

# # Iterate through the country dictionaries returned by the API.
# for country in countries:
#     print(country['names']['common'])
#     print(country['flag']['emoji'])
#     print(country['links']['open_street_maps'])
#     print(f"Population: {country['population']}")
#     print("")