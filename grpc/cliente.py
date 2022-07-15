import sqlite3
import os
import json
import sys
import tela_inicial
import sistema

import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2

'''

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 E TCP
    try:
        client.connect((HOST, PORT))  # tenta se conectar ao servidor
    except Exception as e:
        # se não conseguir mostra esta mensagem de erro
        return print('\nNão foi possível se conectar ao servidor!\n')

    tela_inicial.tela_inicio()
    num = input('Escolha uma das opcoes acima para continuar:')
    tela_inicial.switch_tela_inicio(num, client)

    client.close()


main()
'''
#cliente unario
class UnaryClient(object):
    """
    Cliente para a funcionalidade gRPC 
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)
        
    def get_url(self, message):
        """
        Função do cliente para chamar o rpc para GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    try:
        client = UnaryClient()
        result = client.get_url(message="ola servidor")
        print(f'{result}')

        tela_inicial.tela_inicio()
        num = input('Escolha uma das opcoes acima para continuar:')
        tela_inicial.switch_tela_inicio(num, client)

    except Exception as e:
        print('\nNão foi possível se conectar ao servidor!\n')










