import os
import telas.tela_troca as tela_troca
import operacoes_cliente as cliente


def tela_sistema():
    print('\033[1;36m-----------------------------------------------------------')
    print('\nOlá, você está logado no sistema CarnaTroca.')
    print('-----------------------------------------------------------')
    print('1: Anunciar itens para troca\n''2: Listar todos os itens disponíveis para troca')
    print('3: Ver meus anúncios\n''4: Sair do sistema!\033[m')


def switch_tela_sistema(entrada ,stub, nome):
    if entrada == '1':
        print('\033[1;36mAnunciar fantasias para troca!\033[m')
        nomeFantasia = input('\nNome da fantasia (obrigatório):')
        descricao = input('\nDescrição (opcional):')
        tamanho = input('\nTamanho da fantasia (obrigatório):')
        
        fantasia = cliente.Cliente.criaNovoAnuncio(stub, nomeFantasia, descricao, tamanho, nome)
        print('\033[1;36m-----------------------------------------------------------\033[m')

        if (fantasia == 'aprovado'):        
            os.system('clear')
            print('\033[1;32mFantasia adicionada com sucesso!\033[m')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada, stub, nome)
        else:
            os.system('clear')
            print('\033[1;31mNão foi possível adicionar sua fantasia!!')
            print('Insira os valores válidos nos campos obrigatórios!\033[m')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada, stub, nome)
        

    elif entrada == '2':
        print('\033[1;36mVer todas as fantasias anunciadas do sistema!\033[m')

        lista = cliente.Cliente.listaFantasia(stub, nome)

        if (len(lista) == 0):        
            os.system('clear')
            print('\033[1;31mAinda não há anúncios no sistema!!\033[m')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada, stub, nome)
        else:
            os.system('clear')
            lista = cliente.Cliente.trata_lista(lista)
            lista_tabela = eval(lista)  # esse eval faz o dado voltar a ser lista
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

            tela_troca.tela_troca()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            tela_troca.switch_tela_troca(entrada, stub, nome)


    elif entrada == '3':
        print('\033[1;36mVer todos meus anuncios\033[m')
        
        lista = cliente.Cliente.listaMeusAnuncios(stub, nome)

        if (len(lista) == 0):        
            os.system('clear')
            print('\033[1;31mVocê não possui anuncios no sistema!!\033[m')
            tela_sistema()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            switch_tela_sistema(entrada, stub, nome)
        else:
            os.system('clear')
            lista = cliente.Cliente.trata_lista(lista)
            lista_tabela = eval(lista)  # esse eval faz o dado voltar a ser lista
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
            tela_troca.tela_troca()
            entrada = input('Escolha uma das opcoes acima para continuar:')
            tela_troca.switch_tela_troca(entrada, stub, nome)

    elif entrada == '4':
        print('\033[1;31m\nVocê foi desconectado!\033[m')

    else:
        print('\033[1;31m\nOpcao inválida.\nEscolha uma opção válida!')
        tela_sistema()
        entrada = input('Escolha uma das opcoes acima para continuar:\033[m')
        switch_tela_sistema(entrada, stub, nome)