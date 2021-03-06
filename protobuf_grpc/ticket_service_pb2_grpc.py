# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ticket_service_pb2 as ticket__service__pb2


class TicketServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTicket = channel.unary_unary(
                '/tickets.TicketService/GetTicket',
                request_serializer=ticket__service__pb2.GetTicketRequest.SerializeToString,
                response_deserializer=ticket__service__pb2.Ticket.FromString,
                )
        self.GetCustomerTickets = channel.unary_stream(
                '/tickets.TicketService/GetCustomerTickets',
                request_serializer=ticket__service__pb2.GetCustomerTicketsRequest.SerializeToString,
                response_deserializer=ticket__service__pb2.Ticket.FromString,
                )


class TicketServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTicket(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomerTickets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TicketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTicket': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTicket,
                    request_deserializer=ticket__service__pb2.GetTicketRequest.FromString,
                    response_serializer=ticket__service__pb2.Ticket.SerializeToString,
            ),
            'GetCustomerTickets': grpc.unary_stream_rpc_method_handler(
                    servicer.GetCustomerTickets,
                    request_deserializer=ticket__service__pb2.GetCustomerTicketsRequest.FromString,
                    response_serializer=ticket__service__pb2.Ticket.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tickets.TicketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TicketService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTicket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tickets.TicketService/GetTicket',
            ticket__service__pb2.GetTicketRequest.SerializeToString,
            ticket__service__pb2.Ticket.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCustomerTickets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tickets.TicketService/GetCustomerTickets',
            ticket__service__pb2.GetCustomerTicketsRequest.SerializeToString,
            ticket__service__pb2.Ticket.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
