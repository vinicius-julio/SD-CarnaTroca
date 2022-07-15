import sqlite3
from pydoc import cli
import json
import operacoes_server
import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Opa eu to on e recebi a mensagem "{message}" de você'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve(): 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Aguardando conexao de um cliente...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()