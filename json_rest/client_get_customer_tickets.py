import requests
import json

url = "http://localhost:5000/tickets"

params = {
    "customer_id": 10
}
tickets = requests.get(url, params=params).json()

print(tickets)