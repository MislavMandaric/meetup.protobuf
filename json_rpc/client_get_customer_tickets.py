import requests
import json

url = "http://localhost:5001/api"

payload = {
    "method": "tickets.get_customer_tickets",
    "params": {"customer_id": 10},
    "jsonrpc": "2.0",
    "id": 0,
}
ticket = requests.post(url, json=payload).json()

print(ticket)