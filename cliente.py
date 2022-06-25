import sqlite3
import socket
import os
import json
import sys
import threading


HOST = '127.0.0.1'
PORT = 50000   # cliente só se conecta com o servidor se a porta for a mesma


def tela_inicio():
    print('\n--------------------------------------')
    print('Bem vindo ao CarnaTroca!!')
    print('--------------------------------------')
    print('1: Fazer Cadastro\n''2: Fazer Login\n''3: Sair')


def tela_sistema():
    print('\n--------------------------------------')
    print('Olá, você está logado no sistema CarnaTroca.')
    print('--------------------------------------')
    print('1: Anunciar itens para troca\n''2: Listar todos os itens disponíveis para troca')
    print('3: Ver meus anúncios\n')


def switch_tela_inicio(num, client):
    if num == '1':
        print('\nBora fazer o cadastro')
        user = {
            'nome': input('\nEscolha seu nome de usuario:'),
            'senha': input('Escolha uma senha para sua conta:')
        }

        envio = json.dumps(user)
        # envia a mensagem para o servidor
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        print('---------------------------------------------')
        if (data.decode('utf-8') == 'Aprovado!'):         # decodifica o dado para conseguir ler
            # tela_sistema()
            # os.system('clear')
            print('Cadastro realizado com sucesso!!')
            control = input('Escolha uma das opcoes acima para continuar:')
            tela_sistema(control, client)
        else:
            print('Este nome de usuario já esta cadastradado!')
            print('Tente utilizar outro nome de usuario.')
            tela_inicio()
            num = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_inicio(num, client)

    elif num == '2':
        print('Bora fazer login')
    elif num == '3':
        print('Você foi desconectado do sistema. :/')
        client.close()
    else:
        print('\nOpcao inválida.\nEscolha uma opção válida!')
        tela_inicio()
        num = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_inicio(num, client)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 E TCP
    try:
        client.connect((HOST, PORT))  # tenta se conectar ao servidor
    except Exception as e:
        # se não conseguir mostra esta mensagem de erro
        return print('\nNão foi possível se conectar ao servidor!\n')

    tela_inicio()
    num = input('Escolha uma das opcoes acima para continuar:')
    switch_tela_inicio(num, client)

    print('ENTREI AQUI NO CLOSE')
    client.close()


main()




""""
def switch_tela_sistema(control, client):
    if control == '1':
        print('Anunciar itens para troca!')
    elif control == '2':
        print('Ver todos os itens do sistema!')
    elif control == '3':
        print('Ver todos meus anuncios')
    elif control == '4':
        print('Você foi desconectado do sistema. :/')
        client.close()
    else:
        print('\nOpcao inválida.\nEscolha uma opção válida!')
        tela_sistema()
        num = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_sistema(control, client)
"""