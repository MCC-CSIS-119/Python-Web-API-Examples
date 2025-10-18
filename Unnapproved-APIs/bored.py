import requests

response = requests.get('http://www.boredapi.com/api/activity?participants=2&type=social')
activity = response.json()

for k, v in activity.items():
    print(f'{k}:, {v}')
