class Ticket:
    def __init__(self, ticket_id, customer_id, stake, payout):
        self.ticket_id = ticket_id
        self.customer_id = customer_id
        self.stake = stake
        self.payout = payout

def to_json(tickets):
    if type(tickets) is list:
        return [to_json(ticket) for ticket in tickets]
    
    return {
        "ticket_id": tickets.ticket_id,
        "customer_id": tickets.customer_id,
        "stake": tickets.stake,
        "payout": tickets.payout
    }
