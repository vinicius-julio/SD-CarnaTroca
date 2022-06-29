import sistema
import os
import json

def tela_troca():
    print('\033[1;36m-----------------------------------------------------------')
    print('\nEscolha uma opção para continuar.')
    print('-----------------------------------------------------------')
    print('1: Propor troca.\n''2: Voltar à tela do sistema')
    print('3: Sair\033[m')




def switch_tela_troca(entrada ,client):
    if(entrada == '1'):
        print('PROPOR TROCA!')
        """user = {
            'control' : '(6)',
            'ID_item' :  input('\nID da fantasia que você deseja trocar:'),
        }"""
    


    elif(entrada == '2'):
        os.system('clear')
        sistema.tela_sistema()
        entrada = input('Escolha uma das opcoes acima para continuar:')
        sistema.switch_tela_sistema(entrada,  client)

    elif(entrada == '3'):
        user = {
            'control' : 'quit'
        }
        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)
        if(data.decode() == 'disconnect'):
            print('\033[1;31mVocê foi desconectado do sistema. :/\033[m')
            return


    else:
        print('\033[1;31m\nOpcao inválida.\nEscolha uma opção válida!')
        tela_troca()
        entrada = input('Escolha uma das opcoes acima para continuar:\033[m')
        switch_tela_troca(entrada ,client)
