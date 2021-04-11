import db
from model import to_json

def get_ticket(ticket_id: int) -> dict:
    tickets = db.query_by_ticket_id(ticket_id)

    if len(tickets) == 0:
        raise ValueError('ticket with provided ticket_id not found')
    
    return to_json(tickets[0])

def get_customer_tickets(customer_id: int) -> list:
    tickets = db.query_by_customer_id(customer_id)

    return to_json(tickets)
