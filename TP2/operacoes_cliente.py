import telas.tela_sistema as tela_sistema
import carnatroca_pb2_grpc as pb2_grpc
import carnatroca_pb2 as pb2

class Cliente(object):

    def __init__(self, *args, **kwargs):
        pass

    #trata as mensagens de erro e aprovado
    def trata_mensagem(user):
        new_user = str(user)
        new_user = new_user.split('"')
        new_user = new_user[1]
        return new_user

    #função que trata a mensagem recebida para poder mostrá-la na tela.
    def trata_lista(lista):
            lista = str(lista)
            print(lista)
            lista = lista.split(':')
            lista = lista[1]
            lista = lista.split('"')
            lista = lista[1]
            lista = lista.replace('\\',"")
            return lista

    def cadastraUser(stub, nome, senha):
        user = stub.cadastraUser(pb2.cadUserRequest(nome = nome, senha = senha))
        user = Cliente.trata_mensagem(user)
        return user


    def loginUser(stub, nome, senha):
        user = stub.loginUser(pb2.cadUserRequest(nome = nome, senha = senha))
        user = Cliente.trata_mensagem(user)
        return user
            

    def criaNovoAnuncio(stub, nomeFantasia, descricao, tamanho, nome):
        fantasia = stub.criaNovoAnuncio(pb2.anuncioRequest(nomeFantasia=nomeFantasia, descricao=descricao, tamanho=tamanho, nome=nome))
        fantasia = Cliente.trata_mensagem(fantasia)
        return fantasia

    def listaFantasia(stub, nome):
        lista = stub.listaFantasia(pb2.listaRequest(nome=nome))
        lista = str(lista)
        return lista

    def listaMeusAnuncios(stub, nome):
        lista = stub.listaMeusAnuncios(pb2.listaRequest(nome=nome))
        lista = str(lista)
        return lista


    def proporTroca(stub, ID_item_anunciante, ID_item_proponente, nome):
        ID_item_anunciante = int(ID_item_anunciante)
        ID_item_proponente = int(ID_item_proponente)
        troca = stub.proporTroca(pb2.trocaRequest(ID_item_anunciante=ID_item_anunciante,ID_item_proponente=ID_item_proponente, nome=nome))
        troca = Cliente.trata_mensagem(troca)
        return troca

    def listaTroca(stub, nome):
        troca = stub.listaTroca(pb2.listaTrocaRequest(nome=nome))
        troca = str(troca)
        return troca


    def aceitaTroca(stub, ID_troca, nome):
        ID_troca = int(ID_troca)
        finaliza_troca = stub.aceitaTroca(pb2.finalizaTrocaRequest(ID_troca=ID_troca,nome=nome))
        finaliza_troca = Cliente.trata_mensagem(finaliza_troca)
        return finaliza_troca

    def recusaTroca(stub, ID_troca, nome):
        ID_troca = int(ID_troca)
        finaliza_troca = stub.recusaTroca(pb2.finalizaTrocaRequest(ID_troca=ID_troca,nome=nome))
        finaliza_troca = Cliente.trata_mensagem(finaliza_troca)
        return finaliza_troca