import sqlite3
import socket
import os
import json
import sys
import threading
import tela_inicial
import sistema


HOST = '127.0.0.1'
PORT = 50000   # cliente só se conecta com o servidor se a porta for a mesma

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







