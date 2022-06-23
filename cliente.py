import socket
import json
import threading

HOST = '127.0.0.1'
PORT = 50000   # cliente só se conecta com o servidor se a porta for a mesma


#jsonResult = {"first": "You're", "second": "Awsome!"}
#jsonResult = json.dumps(jsonResult)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 E TCP
    try:
        client.connect((HOST, PORT))  # tenta se conectar ao servidor
    except Exception as e:
        # se não conseguir mostra esta mensagem de erro
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    while True:
        msg = input('O que devemos enviar para o servidor?: ')
        client.sendall(msg.encode('utf-8'))
        if msg == 'sair':
            print('Client está se desconectando!')
            break

        # quando o servidor responde, grava os dados na variavel data
        data = client.recv(1024)
        # decodifica o dado para conseguir ler
        print(f'A resposta do servidor foi:', {data.decode()})

    client.close()


main()
