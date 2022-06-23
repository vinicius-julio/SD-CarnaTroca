from os import system
import socket
import json
import threading

HOST = '127.0.0.1'
PORT = 50000   # cliente só se conecta com o servidor se a porta for a mesma


# jsonResult = {"first": "You're", "second": "Awsome!"}
# jsonResult = json.dumps(jsonResult)

def tela_inicio():
    print('\n--------------------------------------')
    print('Bem vindo ao CarnaTroca!!')
    print('--------------------------------------')
    print('1: Fazer Cadastro\n''2: Fazer Login\n''3: Sair')


def switch(num, client):
    if num == '1':
        print('\nBora fazer o cadastro')
        nome = input('\nEscolha seu nome de usuario:')
        senha = input('Escolha uma senha para sua conta:')
        user = {nome, senha}  # TENHO QUE APRENDER A PASSAR ISSO AQUI
        client.sendall(nome.encode('utf-8'))
        data = client.recv(1024)

        print('---------------------------------------------')
        if (data.decode('utf-8') == 'Aprovado!'):         # decodifica o dado para conseguir ler
            print(f'A resposta do servidor foi:', {data.decode('utf-8')})
        else:
            print(data.decode())
            print('Este nome de usuario já esta cadastradado!')
            print('Tente utilizar outro nome de usuario.')
            tela_inicio()
            num = input('Escolha uma das opcoes acima para continuar:')
            switch(num, client)

    elif num == '2':
        print('Bora fazer login')
    elif num == '3':
        print('Vamos sair!')
    else:
        print('\nOpcao inválida.\nEscolha uma opção válida!\n')
        tela_inicio()
        num = input('Escolha uma das opcoes acima para continuar:')
        switch(num, client)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 E TCP
    try:
        client.connect((HOST, PORT))  # tenta se conectar ao servidor
    except Exception as e:
        # se não conseguir mostra esta mensagem de erro
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    tela_inicio()
    num = input('Escolha uma das opcoes acima para continuar:')
    switch(num, client)

    """while True:
        # system('clear')
        msg = input('O que devemos enviar para o servidor?: ')
        client.sendall(msg.encode('utf-8'))
        if msg == 'sair':
            print('Client está se desconectando!')
            break

        # quando o servidor responde, grava os dados na variavel data
        data = client.recv(1024)
        # decodifica o dado para conseguir ler
        print(f'A resposta do servidor foi:', {data.decode()})"""

    client.close()


main()
