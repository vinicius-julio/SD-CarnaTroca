import os
import json
import troca


def tela_sistema():
    print('\033[1;36m-----------------------------------------------------------')
    print('\nOlá, você está logado no sistema CarnaTroca.')
    print('-----------------------------------------------------------')
    print('1: Anunciar itens para troca\n''2: Listar todos os itens disponíveis para troca')
    print('3: Ver meus anúncios\n''4: Sair do sistema!\033[m')



def switch_tela_sistema(entrada ,client):
    if entrada == '1':
        print('\033[1;36mAnunciar fantasias para troca!\033[m')
        user = {
            'control': ('3'),
            'nome_item': input('\nNome da fantasia (obrigatório):'),
            'descricao' : input('\nDescrição (opcional):'),
            'tamanho' : input('\nTamanho da fantasia (obrigatório):')
        }

        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        print('\033[1;36m-----------------------------------------------------------\033[m')
        if (data.decode('utf-8') == 'Aprovado!'):         # decodifica o dado para conseguir ler
            os.system('clear')
            print('\033[1;32mFantasia adicionada com sucesso!\033[m')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada,  client)
        else:
            os.system('clear')
            print('\033[1;31mNão foi possível adicionar sua fantasia!!')
            print('Insira os valores válidos nos campos obrigatórios!\033[m')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada,  client)

    elif entrada == '2':
        print('\033[1;36mVer todas as fantasias anunciadas do sistema!\033[m')
        user = {
            'control': ('4')
        }
        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        if (data.decode('utf-8') == 'erro'):         # decodifica o dado para conseguir ler
            os.system('clear')
            print('\033[1;31mAinda não há anúncios no sistema!!\033[m')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada,  client)
        else:
            os.system('clear')
        
            lista_tabela = eval(data.decode())  # esse eval faz o dado voltar a ser lista
            linhas = len(lista_tabela) # pego a quantidade de linhas da lista

            print('\033[1;36mLista de fantasias disponíveis para troca:\033[m')
            for i in range(0, linhas):
                print('\033[1;36m-----------------------------------------------------------\033[m')
                print('ID:',str(lista_tabela[i][0]))
                print('Nome do anunciante:',str(lista_tabela[i][1]))
                print('Nome da fantasia:',str(lista_tabela[i][2]))
                print('Descrição:',str(lista_tabela[i][3]))
                print('Tamanho:',str(lista_tabela[i][4]))
                print('Disponivel:', str(lista_tabela[i][5]))  # se for 1 está disponível

            troca.tela_troca()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            troca.switch_tela_troca(entrada,  client)
        
    elif entrada == '3':
        print('\033[1;36mVer todos meus anuncios\033[m')
        user = {
            'control' : ('5')
        }

        envio = json.dumps(user)
        client.sendall(envio.encode('utf-8'))
        data = client.recv(1024)

        if (data.decode('utf-8') == 'erro'):         # decodifica o dado para conseguir ler
            os.system('clear')
            print('\033[1;31mVocê não possui anuncios no sistema!!\033[m')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada,  client)
        else:
            os.system('clear')
        
            lista_tabela = eval(data.decode())  # esse eval faz o dado voltar a ser lista
            linhas = len(lista_tabela) # pego a quantidade de linhas da lista

            print('\033[1;36mMeus anúncios:\033[m')
            for i in range(0, linhas):
                print('\033[1;36m-----------------------------------------------------------\033[m')
                print('ID:',str(lista_tabela[i][0]))
                print('Nome do anunciante:',str(lista_tabela[i][1]))
                print('Nome da fantasia:',str(lista_tabela[i][2]))
                print('Descrição:',str(lista_tabela[i][3]))
                print('Tamanho:',str(lista_tabela[i][4]))
                print('Disponivel:', str(lista_tabela[i][5]))  # se for 1 está disponível

            troca.tela_troca()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            troca.switch_tela_troca(entrada,  client)


    elif entrada == '4':
        print('\033[1;31m\nVocê foi desconectado!\033[m')
        client.close()

    else:
        print('\033[1;31m\nOpcao inválida.\nEscolha uma opção válida!')
        tela_sistema()
        entrada = input('Escolha uma das opcoes acima para continuar:\033[m')
        switch_tela_sistema(entrada ,client)



