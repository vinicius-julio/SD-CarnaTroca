
from venv import create
from flask import Flask, request, jsonify
from flask_restful import Api
import banco_dados.db as bd
from json import dumps


app = Flask(__name__)
app.config['DEBUG']  = True
api = Api(app)


class Servidor():

    @app.route('/cadastraUser', methods=['POST'])
    def cadastraUser():
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        print(f'\n--> Client (Requisição de Cadastro) username: {nome}, senha:{senha}')
        result = bd.cadastroUser_db(nome, senha)
        print(f'--> Retorno da consulta ao banco: {result}')
        return jsonify(result)


    @app.route('/loginUser', methods=['POST'])
    def loginUser():
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        print(f'\n--> Client (Requisição de Login) username: {nome}, senha:{senha}')
        result = bd.loginUser_db(nome, senha)
        print(f'--> Retorno da consulta ao banco: {result}')
        return jsonify(result)


    @app.route('/criaNovoAnuncio', methods=['POST'])
    def criaNovoAnuncio():
        nomeFantasia = request.form.get('nomeFantasia')
        descricao = request.form.get('descricao')
        tamanho = request.form.get('tamanho')
        nome = request.form.get('nome')
        result = bd.criaAnuncio_db(nomeFantasia, descricao, tamanho, nome)
        return jsonify(result)


    @app.route('/listaFantasia', methods=['GET'])
    def listaFantasia():
        nome = request.form.get('nome')
        result = bd.listaFantasia_db(nome)
        return jsonify(result)


    @app.route('/listaMeusAnuncios', methods=['GET'])
    def listaMeusAnuncios():
        nome = request.form.get('nome')
        result = bd.listaMeusAnuncios_bd(nome)
        return jsonify(result)


    @app.route('/proporTroca', methods=['POST'])
    def proporTroca():
        nome = request.form.get('nome')
        ID_item_anunciante = request.form.get('ID_item_anunciante')
        ID_item_proponente = request.form.get('ID_item_proponente')
        result = bd.proporTroca_bd(ID_item_anunciante, ID_item_proponente, nome)
        return jsonify(result)


    @app.route('/listaTroca', methods=['GET'])
    def listaTroca():
        nome = request.form.get('nome')
        result = bd.listaTrocas_db(nome)
        return jsonify(result)


    @app.route('/aceitaTroca', methods=['POST'])
    def aceitaTroca():
        ID_troca = request.form.get('ID_troca')
        nome = request.form.get('nome')
        result = bd.aceitaTroca_db(ID_troca, nome)
        return jsonify(result)


    @app.route('/recusaTroca', methods=['POST'])        
    def recusaTroca():
        ID_troca = request.form.get('ID_troca')
        nome = request.form.get('nome')
        result = bd.recusaTroca_db(ID_troca, nome)
        return jsonify(result)


#server.run (debug = True)
if __name__ == '__main__':
    app.run()