"""Initial countries API example"""

import pprint

import requests


# Prompt user for country and save as string variable named "country_search_pattern"
country_search_pattern = input("What country would like to search for? ")

# Make the GET request to the API endpoint and store response to variable named "response"
response = requests.get(f'https://restcountries.com/v3.1/name/{country_search_pattern}', timeout=10)
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
