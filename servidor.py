import threading
import socket  # faz a comunicação entre o servidor e o cliente

clients = []

HOST = 'localhost'
PORT = 50000


def main():

    # AF_INET(IPV4), SOCK_STREAM(TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # servidor e porta que o socket tem que escutar
    server.bind((HOST, PORT))
    server.listen()     # modo de escuta
    print('Servidor Iniciado\nAguardando conexão dos clientes!')

    while True:
        client, ender = server.accept()  # método para aceitar a conexão
        # adiciona um cliente dentro da lista dos clientes
        clients.append(client)
        print('Novo cliente conectado:')

        # cada cliente que chegar, adicionamos a lista e iniciamos uma thread
        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()


def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:  # pylint: disable=bare-except
            deleteClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:  # se for diferente manda a mensagem
            try:
                clientItem.send(msg)
            except:  # pylint: disable=bare-except
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)


main()
