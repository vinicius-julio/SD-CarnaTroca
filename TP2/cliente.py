import telas.tela_inicial as tela_inicial
import grpc
import carnatroca_pb2_grpc as pb2_grpc
import carnatroca_pb2 as pb2

host = 'localhost'
server_port = 50051


def run ():
    with grpc.insecure_channel('{}:{}'.format(host, server_port)) as channel:
        stub =  pb2_grpc.UnaryStub(channel)
        tela_inicial.tela_inicio()
        num = input('Escolha uma das opcoes acima para continuar:')
        tela_inicial.switch_tela_inicio(num, stub)

  
if __name__ == '__main__':
    run()






