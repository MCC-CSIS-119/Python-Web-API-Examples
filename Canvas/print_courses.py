'''Print Canvas Courses'''
import os
import pprint

import requests


token = path = os.environ["MY_CANVAS_TOKEN"]
headers = {'Authorization': f'Bearer {token}'}

### List courses: https://canvas.instructure.com/doc/api/courses.html#method.courses.index
response = requests.get('https://mcckc.instructure.com/api/v1/courses', headers=headers, timeout=10)
response.raise_for_status()

# 1. Inspect the entire response
pprint.pprint(response.json())

# 2. Step through the items in the response
for item in response.json():
    print(item)
    print("---")

# 3. Print out desired data (Courses)
for course in response.json():
    print(course["name"] + ": " + str(course["id"]))
    print("")
