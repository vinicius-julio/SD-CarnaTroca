import socket
import threading


HOST = 'localhost'
PORT = 50000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 E TCP
server.bind((HOST, PORT))  # Servidor e porta que o socket tem que escutar
server.listen()  # modo de escuta
print('Aguardando conexao de um cliente...')


def novo_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f'Novo cliente conectado em IP:{ip}, e porta:{port}!')
    while True:
        msg = client.recv(1024)  # recebe a mensagem enviada pelo cliente
        if msg.decode() == 'sair':
            break
        print(f'O cliente da porta {port}, disse: {msg.decode()}')
        reply = (f'Voce me disse: {msg.decode()}')
        client.sendall(reply.encode('utf-8'))
    print(f'O cliente do IP:{ip}, e porta:{port}!, foi desconectado!')
    client.close()


while True:
    try:
        client, ip = server.accept()  # server.accept (método para aceitar a conexão)
        thread1 = threading.Thread(target=novo_client, args=[client, ip])
        thread1.start()
    except KeyboardInterrupt:
        print(f'Desligando o servidor!')
        server.close()
