import grpc

import ticket_service_pb2
import ticket_service_pb2_grpc

with grpc.insecure_channel('localhost:5005') as channel:
    client = ticket_service_pb2_grpc.TicketServiceStub(channel)

    tickets = client.GetCustomerTickets(ticket_service_pb2.GetCustomerTicketsRequest(customer_id=10))
    
    for ticket in tickets:
        print(ticket)
