from flask import request, jsonify

import db
from model import to_json

def get_ticket(ticket_id):
    """Endpoint for getting ticket data for provided ID.
    ---
    parameters:
      - name: ticket_id
        in: path
        type: integer
        required: true
    definitions:
      Ticket:
        type: object
        properties:
          ticket_id:
            type: integer
          customer_id:
            type: integer
          stake:
            type: number
          payout:
            type: number
    responses:
      200:
        description: Ticket object
        schema:
          $ref: '#/definitions/Ticket'
      404:
        description: Error message
    """
    tickets = db.query_by_ticket_id(ticket_id)

    if len(tickets) == 0:
        return jsonify({"error": "Not found"}), 404
        
    return jsonify({"data": to_json(tickets[0])})

def get_tickets():
    """Endpoint for getting all ticket data for one customer, by provided customer ID.
    ---
    parameters:
      - name: customer_id
        in: query
        type: integer
        required: true
    definitions:
      TicketList:
        type: array
        items:
          $ref: '#/definitions/Ticket'
      Ticket:
        type: object
        properties:
          ticket_id:
            type: integer
          customer_id:
            type: integer
          stake:
            type: number
          payout:
            type: number
    responses:
      200:
        description: Array of ticket objects
        schema:
          $ref: '#/definitions/TicketList'
    """
    customer_id = request.args.get('customer_id', 0, type=int)

    tickets = db.query_by_customer_id(customer_id)

    return jsonify({"data": to_json(tickets)})

def get_customer_tickets(customer_id):
    """Endpoint for getting all ticket data for one customer, by provided customer ID.
    ---
    parameters:
      - name: customer_id
        in: path
        type: integer
        required: true
    definitions:
      TicketList:
        type: array
        items:
          $ref: '#/definitions/Ticket'
      Ticket:
        type: object
        properties:
          ticket_id:
            type: integer
          customer_id:
            type: integer
          stake:
            type: number
          payout:
            type: number
    responses:
      200:
        description: Array of ticket objects
        schema:
          $ref: '#/definitions/TicketList'
    """
    tickets = db.query_by_customer_id(customer_id)

    return jsonify({"data": to_json(tickets)})