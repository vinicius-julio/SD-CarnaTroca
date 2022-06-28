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
    print('\n----------------------------------------------')
    print('Olá, você está logado no sistema CarnaTroca.')
    print('------------------------------------------------')
    print('1: Anunciar itens para troca\n''2: Listar todos os itens disponíveis para troca')
    print('3: Ver meus anúncios\n')


def switch_tela_inicio(num, client):
    if num == '1':
        print('\nBora fazer o cadastro')
        user = {
            'control': ('1'),
            'nome': input('\nEscolha seu nome de usuario:'),
            'senha': input('Escolha uma senha para sua conta:')
        }

        envio = json.dumps(user)
        # envia a mensagem para o servidor
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        print('---------------------------------------------')
        if (data.decode('utf-8') == 'Aprovado!'):         # decodifica o dado para conseguir ler
            os.system('clear')
            tela_sistema()
            print('Cadastro realizado com sucesso!!')
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada, client)
        else:
            print('Este nome de usuario já esta cadastradado!')
            print('Tente utilizar outro nome de usuario.')
            tela_inicio()
            num = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_inicio(num, client)

    elif num == '2':
        print('Bora fazer login')
        user = {
            'control' : ('2'),
            'nome': input('\nEntre com seu nome de usuario:'),
            'senha': input('Senha:')
        }

        envio = json.dumps(user)
        # envia a mensagem para o servidor
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        print('---------------------------------------------')
        if (data.decode('utf-8') == 'Aprovado!'):         # decodifica o dado para conseguir ler
            os.system('clear')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada, client)
        else:
            print('Credenciais inválidas!')
            print('Informe as credenciais corretas ou crie uma conta.')
            tela_inicio()
            num = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_inicio(num, client)

    elif num == '3':
        print('Você foi desconectado do sistema. :/')
        client.close()
    else:
        print('\nOpcao inválida.\nEscolha uma opção válida!')
        tela_inicio()
        num = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_inicio(num, client)



def switch_tela_sistema(entrada ,client):
    if entrada == '1':
        print('Anunciar fantasias para troca!')
        user = {
            'control': ('3'),
            'nome_item': input('\nNome da fantasia:'),
            'descricao' : input('\nDescrição (opcional):'),
            'tamanho' : input('\nTamanho da fantasia:')
        }

        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        print('---------------------------------------------')
        if (data.decode('utf-8') == 'Aprovado!'):         # decodifica o dado para conseguir ler
            #os.system('clear')
            print('Fantasia adicionada com sucesso!')
        else:
            print('Não foi possível adicionar sua fantasia!!')
            tela_inicio()
            num = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_inicio(num, client)

    elif entrada == '2':
        print('Ver todos as fantasias do sistema!')
        user = {
            'control': ('4')
        }

    elif entrada == '3':
        print('Ver todos meus anuncios')
    elif entrada == '4':
        print('Você foi desconectado do sistema. :/')
        client.close()
    else:
        print('\nOpcao inválida.\nEscolha uma opção válida!')
        tela_sistema()
        num = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_sistema(entrada ,client)




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






