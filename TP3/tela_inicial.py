from ossaudiodev import control_labels
import sistema
import os
import json



def tela_inicio():
    print('\033[1;36m-----------------------------------------------------------')
    print('Bem vindo ao CarnaTroca!!')
    print('-----------------------------------------------------------')
    print('1: Fazer Cadastro\n''2: Fazer Login\n''3: Sair\033[m')



def switch_tela_inicio(num, client):
    if num == '1':
        print('\033[1;36m\nFazer o cadastro\033[m')
        user = {
            'control': ('1'),
            'nome': input('\nEscolha seu nome de usuario:'),
            'senha': input('Escolha uma senha para sua conta:')
        }

        envio = json.dumps(user)
        # envia a mensagem para o servidor
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        print('\033[1;36m-----------------------------------------------------------\033[m')
        if (data.decode('utf-8') == 'Aprovado!'):         # decodifica o dado para conseguir ler
            os.system('clear')
            sistema.tela_sistema()  
            print('\033[1;32mCadastro realizado com sucesso!!\033[m')
            entrada = input('Escolha uma das opcoes acima para continuar:')
            sistema.switch_tela_sistema(entrada, client)
        else:
            print('\033[1;31mEste nome de usuario já esta cadastradado!')
            print('Tente utilizar outro nome de usuario.\033[m')
            tela_inicio() 
            num = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_inicio(num, client)

    elif num == '2':
        print('\033[1;36mBora fazer login\033[m')
        user = {
            'control' : ('2'),
            'nome': input('\nEntre com seu nome de usuario:'),
            'senha': input('Senha:')
        }

        envio = json.dumps(user)
        # envia a mensagem para o servidor
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        print('\033[1;36m-----------------------------------------------------------\033[m')
        if (data.decode('utf-8') == 'Aprovado!'):         # decodifica o dado para conseguir ler
            os.system('clear')
            sistema.tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            sistema.switch_tela_sistema(entrada, client)
        else:
            print('\033[1;31mCredenciais inválidas!')
            print('Informe as credenciais corretas ou crie uma conta.\033[m')
            tela_inicio()
            num = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_inicio(num, client)

    elif num == '3':
        print('\033[1;31m\nVocê foi desconectado!\033[m')
        client.close()

    else:
        print('\033[1;31m\nOpcao inválida.\nEscolha uma opção válida!\033[m')
        tela_inicio()
        num = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_inicio(num, client)