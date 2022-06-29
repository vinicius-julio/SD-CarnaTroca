def cadastra_user(client, cursor, db, nome, senha):
    cursor.execute(f"SELECT user_name FROM user WHERE user_name = '{nome}'")
    verifica = str(cursor.fetchall())  # verifica recebe o conteúdo do select
    if (verifica) != '[]':  # se for != de vazio, signifca que tem dado na tabela
        verifica = verifica.split("'")
        verifica = verifica[1]
        if verifica == nome:
            reply = ('erro')
            client.sendall(reply.encode('utf-8'))
    else:
        # se o nome de usuario for diferente    
        reply = (f'Aprovado!')
        #insere os dados no banco
        cursor.execute(f"INSERT INTO user VALUES ('{nome}','{senha}')")
        db.commit()
        client.sendall(reply.encode('utf-8'))




def faz_login(client, cursor, db, nome, senha):
    cursor.execute(f"SELECT * FROM user WHERE user_name = '{nome}' and senha = '{senha}'")
    verifica = str(cursor.fetchall())  # verifica recebe o conteúdo do select

    if (verifica) == '[]':  # se for == de vazio, signifca que nao achou os dados
        reply = ('erro')   # retorna um erro
        client.sendall(reply.encode('utf-8'))
    else:
        # se o nome de usuario for diferente    
        reply = (f'Aprovado!')
        client.sendall(reply.encode('utf-8'))



def cria_anuncio(client, cursor, db, nome, nome_fantasia, descricao, tamanho):
    print(nome)
    #insere os dados no banco
    if((len(nome_fantasia) == 0) or (len(tamanho) == 0)):
        reply = ('erro')   # retorna um erro
        client.sendall(reply.encode('utf-8'))
    else:
        reply = (f'Aprovado!')
        cursor.execute(f"INSERT INTO fantasias(user_userName, nome_fantasia, descricao, tamanho) VALUES ('{nome}','{nome_fantasia}','{descricao}', '{tamanho}')")
        db.commit()
        client.sendall(reply.encode('utf-8'))



def lista_fantasias(client, cursor, nome):
     # lista todas as fantasias exceto as do usuario
    cursor.execute(f"SELECT * FROM fantasias where user_userName != '{nome}'") 
    lista_tabela = cursor.fetchall()

    if(len(lista_tabela) == 0):
        reply = ('erro')
        client.sendall(reply.encode('utf-8'))
    else:
        reply = (str(lista_tabela))
        client.sendall(reply.encode('utf-8'))




def lista_meus_anuncios(client, cursor, nome):
    cursor.execute(f"SELECT * FROM fantasias where user_userName = '{nome}'") 
    lista_tabela = cursor.fetchall()

    if(len(lista_tabela) == 0):
        reply = ('erro')
        client.sendall(reply.encode('utf-8'))
    else:
        reply = (str(lista_tabela))
        client.sendall(reply.encode('utf-8'))
