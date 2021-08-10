# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class ServiceDatabaseStub(object):
    """interface de serviço
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GerenciaNotas = channel.unary_unary(
                '/ServiceDatabase/GerenciaNotas',
                request_serializer=helloworld__pb2.Request.SerializeToString,
                response_deserializer=helloworld__pb2.Response.FromString,
                )


class ServiceDatabaseServicer(object):
    """interface de serviço
    """

    def GerenciaNotas(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceDatabaseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GerenciaNotas': grpc.unary_unary_rpc_method_handler(
                    servicer.GerenciaNotas,
                    request_deserializer=helloworld__pb2.Request.FromString,
                    response_serializer=helloworld__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ServiceDatabase', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServiceDatabase(object):
    """interface de serviço
    """

    @staticmethod
    def GerenciaNotas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServiceDatabase/GerenciaNotas',
            helloworld__pb2.Request.SerializeToString,
            helloworld__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
