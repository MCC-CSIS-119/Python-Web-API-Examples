import requests
import datetime

your_first_name = "Dan"
your_country_code = "US" # https://countrycode.org/

response = requests.get(f'https://api.agify.io?name={your_first_name}&country_id={your_country_code}')

age_guess = response.json()["age"]
current_date_time = datetime.datetime.now()

print(f"{your_first_name} from {your_country_code} in {current_date_time.year} is {age_guess} years old")
