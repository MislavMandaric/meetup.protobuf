from flask import Flask
from flask_jsonrpc import JSONRPC

import handler

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

jsonrpc.register(handler.get_ticket, "tickets.get_ticket")
jsonrpc.register(handler.get_customer_tickets, "tickets.get_customer_tickets")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)