from concurrent import futures
import logging

import grpc
from grpc_reflection.v1alpha import reflection

import ticket_service_pb2
import ticket_service_pb2_grpc
from handler import TicketServiceServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_service_pb2_grpc.add_TicketServiceServicer_to_server(TicketServiceServicer(), server)

    SERVICE_NAMES = (
        ticket_service_pb2.DESCRIPTOR.services_by_name['TicketService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:5005')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()