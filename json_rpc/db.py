from model import Ticket

tickets_db = [
    Ticket(ticket_id=1, customer_id=10, stake=2, payout=20),
    Ticket(ticket_id=2, customer_id=10, stake=5, payout=20),
    Ticket(ticket_id=3, customer_id=10, stake=10, payout=100),
    Ticket(ticket_id=4, customer_id=20, stake=20, payout=200),
    Ticket(ticket_id=5, customer_id=20, stake=50, payout=100),
    Ticket(ticket_id=6, customer_id=20, stake=100, payout=1000)
]

def query_by_ticket_id(ticket_id):
    return [ticket for ticket in tickets_db if ticket.ticket_id == ticket_id]

def query_by_customer_id(customer_id):
    return [ticket for ticket in tickets_db if ticket.customer_id == customer_id]