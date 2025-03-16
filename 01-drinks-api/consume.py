import requests

response = requests.get('http://localhost:8000/drinks')

print(response.json())  # this will return the JSON representation of all the drinks in the database.  

