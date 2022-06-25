import socket
import threading
import sqlite3
import json


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

    with sqlite3.connect('carna_troca.db') as db:
        while True:
            msg = client.recv(1024)  # recebe a mensagem enviada pelo cliente
            print(msg.decode())
            aux = msg.decode().split('"')  # recebe a mensagem e separa em strings onde tem "
            nome = aux[3] # pega apenas a string que corresponde ao nome de usuario 
            senha = aux[7]  # pega apenas a string que corresponde à senha
            print(nome)
            print(senha)

            cursor = db.cursor()  # possibilita fazer as operações com o banco

            #faz a verificação no banco de dados
            cursor.execute(f"SELECT user_name FROM user WHERE user_name = '{nome}'")
            verifica = str(cursor.fetchall())  # verifica recebe o conteúdo do select
            if (verifica) != '[]':  # se for != de vazio, signifca que tem dado na tabela
                verifica = verifica.split("'")
                verifica = verifica[1]
                if verifica == nome:
                    reply = ('erro')
                    client.sendall(reply.encode('utf-8'))
            else:
                # se o nome de usuario for diferente
                print(f'O cliente da porta {port}, disse: {msg.decode()}')
                reply = (f'Aprovado!')
                # insere os dados no banco
                cursor.execute(f"INSERT INTO user VALUES ('{nome}','{senha}')")
                db.commit()
                client.sendall(reply.encode('utf-8'))


def threads():
    while True:
        try:
            client, ip = server.accept()  # server.accept (método para aceitar a conexão)
            thread1 = threading.Thread(target=novo_client, args=[client, ip])
            thread1.start()
        except KeyboardInterrupt:
            print(f'Desligando o servidor!')
            server.close()


threads()
