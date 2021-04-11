from flask import Flask
from flasgger import Swagger

import handler

app = Flask(__name__)
swagger = Swagger(app)

app.add_url_rule('/tickets/<int:ticket_id>', methods=['GET'], view_func=handler.get_ticket)
app.add_url_rule('/tickets', methods=['GET'], view_func=handler.get_tickets)
app.add_url_rule('/customers/<int:customer_id>/tickets', methods=['GET'], view_func=handler.get_customer_tickets)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)