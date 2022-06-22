
import threading
import socket


HOST = 'localhost'
PORT = 50000

'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))    # conecta com o servidor
# envia os dados para o servidor
client.sendall(str.encode('Bom dia Servidor!'))

# quando o servidor responde, grava os dados na variavel data
data = client.recv(1024)

# decodifica o dado para conseguir ler
print('Mnesagem retornada!', data.decode())'''


def main():
    # AF_INET(IPV4), SOCK_STREAM(TCP)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))  # tenta se conectar ao servidor
    except:  # pylint: disable=bare-except
        # se não conseguir mostra esta mensagem de erro
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    print('Olá, bem vindo ao CarnaTroca!')
    print('Escolha uma opção para continuar:\n')

    nav = 0
    # while nav != '2':
    nav = input('1 - Fazer Cadastro\n2 - Fazer Login\n')

    if nav == '1':  # fazer o cadastro (e-mail, senha, nome e cpf)
        userName = input('Nome de usuario: ')
        cpf = input('Informe o CPF: ')
        email = input('Email: ')
        senha = input('Senha: ')
        print('Conta criada com sucesso!')

    elif nav == '2':
        userName = input('Informe seu nome de usuario: ')
        senha = input('Senha: ')
        print('Conetado!')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, userName])

    thread1.start()
    thread2.start()



def receiveMessages(client):  # função para receber as mensagens
    while True:
        try:
            # decodifica o dado para conseguir ler
            msg = client.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:  # pylint: disable=bare-except
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break



def sendMessages(client, userName):  # função para enviar as mensagens
    while True:
        try:
            msg = input('\n')
            client.send(f'<{userName}> {msg}'.encode('utf-8'))
        except:
            return


main()
