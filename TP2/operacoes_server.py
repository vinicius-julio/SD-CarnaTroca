import carnatroca_pb2_grpc as pb2_grpc
import carnatroca_pb2 as pb2
import banco_dados.bd as bd

class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass


    def cadastraUser(self, request, context):
        nome = request.nome
        senha = request.senha
        sql = bd.cadastroUser_db(nome, senha)
        return pb2.cadUserResponse(message = sql)


    def loginUser(self, request, context):
        nome = request.nome
        senha = request.senha
        sql = bd.loginUser_db(nome, senha)
        return pb2.cadUserResponse(message = sql)

    
    def criaNovoAnuncio(self, request, context):
        nomeFantasia = request.nomeFantasia
        descricao = request.descricao
        tamanho = request.tamanho
        nome = request.nome
        sql = bd.criaAnuncio_db(nomeFantasia, descricao, tamanho, nome)
        return pb2.anuncioResponse(message = sql)
        

    def listaFantasia(self, request, context):
        nome = request.nome
        sql = bd.listaFantasia_db(nome)
        return pb2.listaResponse(message = sql)

    
    def listaMeusAnuncios(self, request, context):
        nome = request.nome
        sql = bd.listaMeusAnuncios_bd(nome)
        return pb2.listaResponse(message = sql)

    def proporTroca(self, request, context):
        nome = request.nome
        ID_item_anunciante = request.ID_item_anunciante
        ID_item_proponente = request.ID_item_proponente
        sql = bd.proporTroca_bd(ID_item_anunciante, ID_item_proponente, nome)
        return pb2.trocaResponse(message=sql)

    
    def listaTroca(self, request, context):
        nome = request.nome
        sql = bd.listaTrocas_db(nome)
        return pb2.listaTrocaResponse(message = sql)


    def aceitaTroca(self, request, context):
        ID_troca = request.ID_troca
        nome = request.nome
        sql = bd.aceitaTroca_db(ID_troca, nome)
        return pb2.finalizaTrocaResponse(message=sql)

    def recusaTroca(self, request, context):
        ID_troca = request.ID_troca
        nome = request.nome
        sql = bd.recusaTroca_db(ID_troca, nome)
        return pb2.finalizaTrocaResponse(message=sql)