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
        cursor.execute(f"INSERT INTO fantasias(user_userName, nome_fantasia, descricao, tamanho, disponivel) VALUES ('{nome}','{nome_fantasia}','{descricao}', '{tamanho}', '1')")
        db.commit()
        client.sendall(reply.encode('utf-8'))



def lista_fantasias(client, cursor, nome):
     # lista todas as fantasias exceto as do usuario
    cursor.execute(f"SELECT * FROM fantasias where user_userName != '{nome}' and disponivel = '1'") 
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



def propor_troca(client, db, cursor, nome, ID_fantasia_anunciante, ID_fantasia_proponente):
    cursor.execute(f"SELECT * FROM fantasias where ID = '{ID_fantasia_anunciante}' and disponivel = '1'")
    verifica = str(cursor.fetchall())
    cursor.execute(f"SELECT * FROM fantasias where ID = '{ID_fantasia_proponente}' and user_userName = '{nome}' and disponivel = '1'")
    verifica2 = str(cursor.fetchall())

    if ((verifica) == '[]') or ((verifica2) == '[]'):  # se for == de vazio, signifca que nao achou os dados
        reply = ('erro')   # retorna um erro
        client.sendall(reply.encode('utf-8'))
    else:
        reply = (f'Aprovado!')
        cursor.execute(f"UPDATE fantasias SET disponivel = '0' where ID = '{ID_fantasia_anunciante}'") 
        cursor.execute(f"UPDATE fantasias SET disponivel = '0' where ID = '{ID_fantasia_proponente}'")
        cursor.execute(f"INSERT INTO trocas_pendentes (ID_anunciante, ID_proponente, nome_proponente) VALUES ('{ID_fantasia_anunciante}','{ID_fantasia_proponente}','{nome}')")
        db.commit()
        client.sendall(reply.encode('utf-8'))



def monitorar_trocas(client, cursor, nome):
    cursor.execute(f"""SELECT F.ID,
                                F.user_userName,
                                F.nome_fantasia,
                                F.descricao,
                                F.tamanho,
                                T.ID_troca
                        FROM fantasias as F
                        INNER JOIN trocas_pendentes as T
                        ON ((F.ID = T.ID_anunciante and F.user_userName = '{nome}')
                        or (F.ID = T.ID_proponente and F.user_userName = T.nome_proponente))""")
    
    monitora_troca = cursor.fetchall()
    if(len(monitora_troca) == 0):
        reply = ('erro')
        client.sendall(reply.encode('utf-8'))
    else:
        reply = (str(monitora_troca))
        client.sendall(reply.encode('utf-8'))



def aceita_trocas(client, cursor, db, nome, ID_troca):
    cursor.execute(f"SELECT * FROM trocas_pendentes where ID_troca = '{ID_troca}'")
    verifica = str(cursor.fetchall())
    if ((verifica) == '[]'):  # se for == de vazio, signifca que nao achou os dados
        reply = ('erro')   # retorna um erro
        client.sendall(reply.encode('utf-8'))
    else:
        reply = (f'Aprovado!')

        cursor.execute(f"""UPDATE fantasias
                            SET user_userName = '{nome}'
                            FROM trocas_pendentes as T
                            WHERE(fantasias.ID = T.ID_proponente)""")

        cursor.execute(f"""UPDATE fantasias
                            SET user_userName = T.nome_proponente
                            FROM trocas_pendentes as T
                            WHERE(fantasias.ID = T.ID_anunciante)""")


        cursor.execute(f"""INSERT INTO controle_trocas(ID_troca, 
                                                        ID_fantasia_anunciante,
                                                        ID_fantasia_proponente) 
                                                        SELECT T.ID_troca,
                                                                T.ID_anunciante,
                                                                T.ID_proponente
                                                        FROM trocas_pendentes as T""")
        cursor.execute(f"UPDATE controle_trocas SET resultado_troca = '1' WHERE ID_troca = '{ID_troca}'")
        cursor.execute(f"DELETE FROM trocas_pendentes WHERE ID_troca = '{ID_troca}'")
        db.commit()
        client.sendall(reply.encode('utf-8'))


def recusa_trocas(client, cursor, db, nome, ID_troca):
    cursor.execute(f"SELECT * FROM trocas_pendentes where ID_troca = '{ID_troca}'")
    verifica = str(cursor.fetchall())
    if ((verifica) == '[]'):  # se for == de vazio, signifca que nao achou os dados
        reply = ('erro')   # retorna um erro
        client.sendall(reply.encode('utf-8'))
    else:
        reply = (f'Aprovado!')
        cursor.execute(f"""UPDATE fantasias
                            SET disponivel = '1'
                            FROM trocas_pendentes as T
                            WHERE(((fantasias.ID = T.ID_anunciante) or (fantasias.ID = T.ID_proponente))
                            and T.ID_troca = '{ID_troca}')""")



        cursor.execute(f"""INSERT INTO controle_trocas(ID_troca, 
                                                        ID_fantasia_anunciante,
                                                        ID_fantasia_proponente) 
                                                        SELECT T.ID_troca,
                                                                T.ID_anunciante,
                                                                T.ID_proponente
                                                        FROM trocas_pendentes as T""")
        cursor.execute(f"UPDATE controle_trocas SET resultado_troca = '0' WHERE ID_troca = '{ID_troca}'")
        cursor.execute(f"DELETE FROM trocas_pendentes WHERE ID_troca = '{ID_troca}'")
        db.commit()
        client.sendall(reply.encode('utf-8'))