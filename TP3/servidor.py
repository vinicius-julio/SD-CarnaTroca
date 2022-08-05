from pydoc import cli
import socket
import threading
import sqlite3
import json
import operacoes_server


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
            aux = msg.decode('utf-8').split('"')  # recebe a mensagem e separa em strings onde tem "
            print(aux)
            control = aux[3]  # pega o valor de controle
            
            cursor = db.cursor()  # possibilita fazer as operações com o banco

            if(control == '1'):  #se o control for 1 ele faz a operação de cadastrar usuario
                nome = aux[7] # pega apenas a string que corresponde ao nome de usuario 
                senha = aux[11]  # pega apenas a string que corresponde à senha
                operacoes_server.cadastra_user(client, cursor, db, nome, senha)
            elif(control == '2'):
                nome = aux[7] # pega apenas a string que corresponde ao nome de usuario 
                senha = aux[11]  # pega apenas a string que corresponde à senha
                operacoes_server.faz_login(client, cursor, db, nome, senha)
            elif (control == '3'):
                nome_fantasia = aux[7] # pega a string que corresponde ao nome da fantasia
                descricao = aux[11] # pega a string que corresponde a descrição da fantasia
                tamanho = aux[15]  # pega a string que corresponde ao tamanho
                operacoes_server.cria_anuncio(client, cursor, db, nome, nome_fantasia, descricao, tamanho)
            elif(control == '4'):
                operacoes_server.lista_fantasias(client, cursor, nome)
            elif(control == '5'):
                operacoes_server.lista_meus_anuncios(client, cursor, nome)
            elif(control == '6'):
                ID_fantasia_anunciante = aux[7]
                ID_fantasia_proponente = aux[11]
                operacoes_server.propor_troca(client, db, cursor, nome, ID_fantasia_anunciante, ID_fantasia_proponente)
            elif(control == '7'):
                operacoes_server.monitorar_trocas(client, cursor, nome)
                
            elif (control == 'aceita_troca'):
                ID_troca = aux[7]
                operacoes_server.aceita_trocas(client, cursor, db, nome, ID_troca)
                
            elif (control == 'recusa_troca'):
                ID_troca = aux[7]
                operacoes_server.recusa_trocas(client, cursor, db, nome, ID_troca)

                


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
