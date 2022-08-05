import telas.tela_inicial as tela_inicial
import requests

class Cliente(object):

    def __init__(self, *args, **kwargs):
        pass

    def run ():
        tela_inicial.tela_inicio()
        num = input('Escolha uma das opcoes acima para continuar:')
        tela_inicial.switch_tela_inicio(num)


    def cadastraUser(nome, senha):
        request = requests.post('http://localhost:5000/cadastraUser',data = {'nome': nome, 'senha':senha})
        resultado = request.json()
        return resultado


    def loginUser(nome, senha):
        request = requests.post('http://localhost:5000/loginUser',data = {'nome': nome, 'senha':senha})
        resultado = request.json()
        return resultado

            
    def criaNovoAnuncio(nomeFantasia, descricao, tamanho, nome):
        request = requests.post('http://localhost:5000/criaNovoAnuncio',
        data = {'nomeFantasia': nomeFantasia, 'descricao':descricao, 'tamanho': tamanho, 'nome':nome})
        resultado = request.json()
        return resultado

    def listaFantasia(nome):
        request = requests.get('http://localhost:5000/listaFantasia',data = {'nome': nome})
        resultado = request.json()
        return resultado

    def listaMeusAnuncios(nome):
        request = requests.get('http://localhost:5000/listaMeusAnuncios',data = {'nome': nome})
        resultado = request.json()
        return resultado


    def proporTroca(ID_item_anunciante, ID_item_proponente, nome):
        ID_item_anunciante = int(ID_item_anunciante)
        ID_item_proponente = int(ID_item_proponente)
        request = requests.post('http://localhost:5000/proporTroca',
        data = {'ID_item_anunciante': ID_item_anunciante, 'ID_item_proponente': ID_item_proponente,'nome': nome})
        resultado = request.json()
        return resultado


    def listaTroca(nome):
        request = requests.get('http://localhost:5000/listaTroca',data = {'nome': nome})
        resultado = request.json()
        return resultado


    def aceitaTroca(ID_troca, nome):
        ID_troca = int(ID_troca)
        request = requests.post('http://localhost:5000/aceitaTroca',data = {'ID_troca': ID_troca,'nome': nome})
        resultado = request.json()
        return resultado

    def recusaTroca(ID_troca, nome):
        ID_troca = int(ID_troca)
        request = requests.post('http://localhost:5000/recusaTroca',data = {'ID_troca': ID_troca,'nome': nome})
        resultado = request.json()
        return resultado

  
  
if __name__ == '__main__':
    Cliente.run()
