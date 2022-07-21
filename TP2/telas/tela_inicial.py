import os
import telas.tela_sistema as tela_sistema
import operacoes_cliente as cliente

def tela_inicio():
    print('\033[1;36m-----------------------------------------------------------')
    print('Bem vindo ao CarnaTroca!!')
    print('-----------------------------------------------------------')
    print('1: Fazer Cadastro\n''2: Fazer Login\n''3: Sair\033[m')


def switch_tela_inicio(num, stub):
    if num == '1':
        print('\033[1;36m\nFazer o cadastro\033[m')
        print('\033[1;36m-----------------------------------------------------------\033[m')

        nome = input('Escolha seu nome de usuario:')
        senha = input('Escolha uma senha para sua conta:')
        user = cliente.Cliente.cadastraUser(stub, nome, senha)

        if (user == 'aprovado'):      
            os.system('clear')
            print('\033[1;32mCadastro realizado com sucesso!!\033[m')
            tela_sistema.tela_sistema()  
            entrada = input('Escolha uma das opcoes acima para continuar:')
            tela_sistema.switch_tela_sistema(entrada, stub, nome)
        else:
            print('\033[1;31mNome de usuario invalido!')
            print('Tente utilizar outro nome de usuario.\033[m')
            tela_inicio() 
            num = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_inicio(num, stub)

    elif num == '2':
        print('\033[1;36mBora fazer login\033[m')
        print('\033[1;36m-----------------------------------------------------------\033[m')
        nome = input('\nEntre com seu nome de usuario:')
        senha = input('Senha:')
        user = cliente.Cliente.loginUser(stub, nome, senha)
        
        if (user == 'aprovado'):       
            os.system('clear')
            tela_sistema.tela_sistema()  
            entrada = input('Escolha uma das opcoes acima para continuar:')
            tela_sistema.switch_tela_sistema(entrada, stub, nome)
        else:
            print('\033[1;31mNome de usuario invalido!')
            print('Tente utilizar outro nome de usuario.\033[m')
            tela_inicio() 
            num = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_inicio(num, stub)

    elif num == '3':
        print('\033[1;31m\nVocê foi desconectado!\033[m')

    else:
        print('\033[1;31m\nOpcao inválida.\nEscolha uma opção válida!\033[m')
        tela_inicio()
        num = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_inicio(num, stub)
