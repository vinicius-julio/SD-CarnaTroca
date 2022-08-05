#aqui estão as operações do banco de dados
import sqlite3


def cadastroUser_db(nome, senha):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT user_name FROM user WHERE user_name = '{nome}'")
    verifica = str(cursor.fetchall())  # verifica recebe o conteúdo do select
    if (verifica) != '[]':  # se for != de vazio, signifca que tem dado na tabela
        return 'erro'
    else:
        cursor.execute(f"INSERT INTO user VALUES ('{nome}','{senha}')")
        db.commit()
        return 'aprovado' 


def loginUser_db(nome, senha):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM user WHERE user_name = '{nome}' and senha = '{senha}'")
    verifica = str(cursor.fetchall())  # verifica recebe o conteúdo do select
    print(verifica)
    if (verifica) == '[]': 
        return 'erro'
    else:
        return 'aprovado' 



def criaAnuncio_db(nome_fantasia, descricao, tamanho, nome):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()
    if((len(nome_fantasia) == 0) or (len(tamanho) == 0)):
        return 'erro'   # retorna um erro
    else:
        cursor.execute(f"INSERT INTO fantasias(user_userName, nome_fantasia, descricao, tamanho, disponivel) VALUES ('{nome}','{nome_fantasia}','{descricao}', '{tamanho}', '1')")
        db.commit()
        return 'aprovado'


def listaFantasia_db(nome):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM fantasias where user_userName != '{nome}' and disponivel = '1'") 
    lista_tabela = cursor.fetchall()

    if(len(lista_tabela) == 0):
        return None  
    else:
        aux = (str(lista_tabela))
        return aux


def listaMeusAnuncios_bd(nome):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM fantasias where user_userName = '{nome}'") 
    lista_tabela = cursor.fetchall()

    if(len(lista_tabela) == 0):
        return None
    else:
        aux = (str(lista_tabela))
        return aux



def proporTroca_bd(ID_item_anunciante, ID_item_proponente, nome):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()

    cursor.execute(f"SELECT * FROM fantasias where ID = '{ID_item_anunciante}' and disponivel = '1'")
    verifica = str(cursor.fetchall())
    cursor.execute(f"SELECT * FROM fantasias where ID = '{ID_item_proponente}' and user_userName = '{nome}' and disponivel = '1'")
    verifica2 = str(cursor.fetchall())

    if ((verifica) == '[]') or ((verifica2) == '[]'):  # se for == de vazio, signifca que nao achou os dados
        return 'erro'
    else:
        cursor.execute(f"UPDATE fantasias SET disponivel = '0' where ID = '{ID_item_anunciante}'") 
        cursor.execute(f"UPDATE fantasias SET disponivel = '0' where ID = '{ID_item_proponente}'")
        cursor.execute(f"INSERT INTO trocas_pendentes (ID_anunciante, ID_proponente, nome_proponente) VALUES ('{ID_item_anunciante}','{ID_item_proponente}','{nome}')")
        db.commit()
        return 'aprovado'
        


def listaTrocas_db(nome):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()
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
        return None
    else:
        aux = (str(monitora_troca))
        return aux


def aceitaTroca_db(ID_troca, nome):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()

    cursor.execute(f"SELECT * FROM trocas_pendentes where ID_troca = '{ID_troca}'")
    verifica = str(cursor.fetchall())

    if ((verifica) == '[]'):  # se for == de vazio, signifca que nao achou os dados
        return 'erro'
    else:
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
        return 'aprovado'

    

def recusaTroca_db(ID_troca, nome):
    db = sqlite3.connect('carna_troca.db')
    cursor = db.cursor()

    cursor.execute(f"SELECT * FROM trocas_pendentes where ID_troca = '{ID_troca}'")
    verifica = str(cursor.fetchall())

    if ((verifica) == '[]'):  # se for == de vazio, signifca que nao achou os dados
        return 'erro'
    else:
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
        return 'aprovado'