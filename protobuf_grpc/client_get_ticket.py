import grpc

import ticket_service_pb2
import ticket_service_pb2_grpc

with grpc.insecure_channel('localhost:5005') as channel:
    client = ticket_service_pb2_grpc.TicketServiceStub(channel)

    ticket = client.GetTicket(ticket_service_pb2.GetTicketRequest(ticket_id=1))
    
    print(ticket)
