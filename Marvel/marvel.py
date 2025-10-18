import requests

params = {'ts': '2023-11-1912:07:51', 'apikey': '123abc', 'hash': '1q2w3e4r5t6y7u'}
base_url = 'http://gateway.marvel.com/v1/public'

response = requests.get(f'{base_url}/characters', params=params, timeout=10)
characters_data = response.json()
