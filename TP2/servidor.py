import grpc
from concurrent import futures
import carnatroca_pb2_grpc as pb2_grpc
import carnatroca_pb2 as pb2
import operacoes_server


def serve(): 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(operacoes_server.UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Aguardando conexao de um cliente...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()