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


def cadastra_user(client, cursor, db, nome, senha):
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
        reply = (f'Aprovado!')
        # insere os dados no banco
        #cursor.execute(f"INSERT INTO user VALUES ('{nome}','{senha}')")
        #db.commit()
        client.sendall(reply.encode('utf-8'))


def faz_login(client, cursor, db, nome, senha):
    cursor.execute(f"SELECT * FROM user WHERE user_name = '{nome}' and senha = '{senha}'")
    verifica = str(cursor.fetchall())  # verifica recebe o conteúdo do select

    if (verifica) == '[]':  # se for == de vazio, signifca que nao achou os dados
        reply = ('erro')   # retorna um erro
        client.sendall(reply.encode('utf-8'))
    else:
        # se o nome de usuario for diferente    
        reply = (f'Aprovado!')
        client.sendall(reply.encode('utf-8'))



def cria_anuncio(client, cursor, db, nome, nome_fantasia, descricao, tamanho):
    reply = (f'Aprovado!')
    print(nome)
    print(nome_fantasia)
    #insere os dados no banco
    #cursor.execute(f"INSERT INTO fantasias VALUES ('{nome}','{nome_fantasia}','{descricao}', '{tamanho}')")
    #db.commit()
    client.sendall(reply.encode('utf-8'))




def novo_client(client, connection):

    ip = connection[0]
    port = connection[1]
    print(f'Novo cliente conectado em IP:{ip}, e porta:{port}!')

    with sqlite3.connect('carna_troca.db') as db:
        while True:
            msg = client.recv(1024)  # recebe a mensagem enviada pelo cliente
            print(msg.decode())
            aux = msg.decode().split('"')  # recebe a mensagem e separa em strings onde tem "
            control = aux[3]  # pega o valor de controle

            cursor = db.cursor()  # possibilita fazer as operações com o banco

            if(control == '1'):  #se o control for 1 ele faz a operação de cadastrar usuario
                nome = aux[7] # pega apenas a string que corresponde ao nome de usuario 
                senha = aux[11]  # pega apenas a string que corresponde à senha
                cadastra_user(client, cursor, db, nome, senha)
            elif(control == '2'):
                nome = aux[7] # pega apenas a string que corresponde ao nome de usuario 
                senha = aux[11]  # pega apenas a string que corresponde à senha
                faz_login(client, cursor, db, nome, senha)
            elif (control == '3'):
                nome_fantasia = aux[7]
                descricao = aux[11]
                tamanho = aux[15]
                cria_anuncio(client, cursor, db, nome, nome_fantasia, descricao, tamanho)
                


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
