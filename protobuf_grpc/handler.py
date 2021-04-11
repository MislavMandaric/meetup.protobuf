import db
import ticket_service_pb2
import ticket_service_pb2_grpc

class TicketServiceServicer(ticket_service_pb2_grpc.TicketServiceServicer):

    def GetTicket(self, request, context):
        tickets = db.query_by_ticket_id(request.ticket_id)

        if len(tickets) == 0:
            return ticket_service_pb2.Ticket()

        return tickets[0]

    def GetCustomerTickets(self, request, context):
        tickets = db.query_by_customer_id(request.customer_id)

        for ticket in tickets:
            yield ticket