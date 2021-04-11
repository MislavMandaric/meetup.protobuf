import requests
import json

url = "http://localhost:5000/tickets/1"

ticket = requests.get(url).json()

print(ticket)