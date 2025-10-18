import requests

# number is
#   - an integer, or
#   - a the keyword random, for which we will try to return a random available fact, or
#   - a a day of year in the form month/day (eg. 2/29, 1/09, 04/1), if type is date
#   - a ranges of numbers
number = 42

# type is one of trivia, math, date, or year. Defaults to trivia if omitted.
type = 'trivia'

headers = {'Content-Type': 'application/json'}
base_url = 'http://numbersapi.com'

response = requests.get(f'{base_url}/{number}/{type}', headers=headers)
print(response.json())
