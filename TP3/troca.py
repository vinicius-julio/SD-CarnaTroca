import sistema
import os
import json

def tela_troca():
    print('\033[1;36m-----------------------------------------------------------')
    print('\nEscolha uma opção para continuar.')
    print('-----------------------------------------------------------')
    print('1: Propor troca.\n''2: Listar as propostas de troca\n''3: Voltar à tela do sistema')
    print('4: Sair\033[m')



def tela_troca2():
    print('\033[1;36mDeseja aceitar ou recusar a(s) troca(s)?\033[m')
    print('\033[1;36m1 - Aceitar\n2 - Recusar\033[m')


def switch_tela_troca2(troca ,client):
    if(troca == '1'):
        user = {
            'control' : 'aceita_troca',
            'id_troca': input('\nInforme o ID da troca que deseja aceitar: ')
        }
        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        if (data.decode('utf-8') == 'erro'):         # decodifica o dado para conseguir ler
            os.system('clear')
            print('\033[1;31mOcorreu pois você informou o ID da troca errado!!\033[m')
            print('\033[1;31mInforme um ID correto!!\033[m')
            tela_troca2()
            troca = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_troca2(troca,  client)
        else:
            os.system('clear')
            print('\033[1;36mTroca efetuada com sucesso!\033[m')
            tela_troca()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_troca(entrada,  client)

    elif(troca == '2'):  #RECUSA A TROCA
        user = {
            'control' : 'recusa_troca',
            'id_troca': input('\nInforme o ID da troca que deseja recusar: ')
        }
        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)
        if (data.decode('utf-8') == 'erro'):         # decodifica o dado para conseguir ler
            os.system('clear')
            print('\033[1;31mOcorreu pois você informou o ID da troca errado!!\033[m')
            print('\033[1;31mInforme um ID correto!!\033[m')
            tela_troca2()
            troca = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_troca2(troca,  client)

        else:
            os.system('clear')
            print('\033[1;36mTroca recusada!\033[m')
        
        tela_troca()
        entrada = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_troca(entrada,  client)


def switch_tela_troca(entrada ,client):
    if(entrada == '1'):
        print('\033[1;36mPROPOR TROCA!\033[m')
        user = {
            'control' : '6',
            'ID_item_anunciante' :  input('\nID da fantasia que você deseja:'),
            'ID_item_proponente' : input('\nID da fantasia que você deseja propor em troca: ')
        }
    
        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        if (data.decode('utf-8') == 'erro'):         # decodifica o dado para conseguir ler
            os.system('clear')
            print('\033[1;31mOcorreu um erro ao solicitar a troca de fantasias!!\033[m')
            print('\033[1;31mUma das fantasias já está em operação de troca!!\033[m')
            tela_troca()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_troca(entrada,  client)
        else:
            os.system('clear')
            print('\033[1;36mSeu pedido de troca foi enviado ao anunciante!!\033[m')
            print('\033[1;36mAguarde até que ele responda!!\033[m')

        tela_troca()
        entrada = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_troca(entrada,  client)



    elif(entrada == '2'):
        print('\033[1;36mListando suas propostas de troca!\033[m')
        user = {
            'control' : '7'
        }

        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        if (data.decode('utf-8') == 'erro'):         # decodifica o dado para conseguir ler
            os.system('clear')
            print('\033[1;31mOcorreu um erro ao listar suas operações de troca!!\033[m')
            print('\033[1;31mVocê não possui trocas pendentes!!\033[m')
            tela_troca()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_troca(entrada,  client)
        else:
            os.system('clear')
            print('\033[1;36mListando suas propostas de troca:\033[m')

            monitora_troca = eval(data.decode())  # esse eval faz o dado voltar a ser lista
            linhas = len(monitora_troca) # pego a quantidade de linhas da lista
            
            if (linhas % 2) == 0:
                for i in range(0, linhas, 2):
                    print('\033[1;36mMinha fantasia:\033[m')
                    print('ID:',str(monitora_troca[i][0]))
                    print('Nome do anunciante:',str(monitora_troca[i][1]))
                    print('Nome da fantasia:',str(monitora_troca[i][2]))
                    print('Descrição:',str(monitora_troca[i][3]))
                    print('Tamanho:',str(monitora_troca[i][4]))
                    print('ID_Troca:',str(monitora_troca[i][5]))
                    print('\033[1;36mFantasia proposta em troca:\033[m')
                    print('ID:',str(monitora_troca[i+1][0]))
                    print('Nome do anunciante:',str(monitora_troca[i+1][1]))
                    print('Nome da fantasia:',str(monitora_troca[i+1][2]))
                    print('Descrição:',str(monitora_troca[i+1][3]))
                    print('Tamanho:',str(monitora_troca[i+1][4]))
                    print('ID_Troca:',str(monitora_troca[i+1][5]))
                    print('\033[1;36m-----------------------------------------------------------\033[m')
            else:
                print('\033[1;31m\nNão há propostas para você!\033[m')
                tela_troca()
                troca = input('Escolha uma das opcoes acima para continuar:')
                switch_tela_troca(troca, client)

       
        tela_troca2()
        troca = input('Escolha uma das opcoes acima para continuar:')
        switch_tela_troca2(troca, client)
        


    elif(entrada == '3'):
        os.system('clear')
        sistema.tela_sistema()
        entrada = input('Escolha uma das opcoes acima para continuar:')
        sistema.switch_tela_sistema(entrada,  client)
        

    elif(entrada == '4'):
        print('\033[1;31m\nVocê foi desconectado!\033[m')
        client.close()


    else:
        print('\033[1;31m\nOpcao inválida.\nEscolha uma opção válida!')
        tela_troca()
        entrada = input('Escolha uma das opcoes acima para continuar:\033[m')
        switch_tela_troca(entrada ,client)
