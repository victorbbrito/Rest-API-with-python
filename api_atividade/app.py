from flask import Flask

from flask import request

from flask_restful import Resource

from flask_restful import Api

from flask_httpauth import HTTPBasicAuth

from models import Pessoas

from models import Atividades

from models import Usuarios

auth = HTTPBasicAuth()

app = Flask(__name__)

api = Api(app)

USUARIOS = {
    'victor' : '1234',
    'rafael' : '1234',
    'brito' : '040506'
}

@auth.verify_password()
def check(login, password):
    if not (login,password):
        return False
    
    return Usuarios.query.filter_by(login = login, password = password, status = True).first()
    

class Pessoa(Resource):
    
    def get(self, name):
        pessoa = Pessoas.query.filter_by(name=name).first()
        try:
            
            response = {
                'nome' : pessoa.name,
                'idade' : pessoa.age,
                'id' : pessoa.id
            }
            
        except AttributeError:
            
            response = {
                'status':'error',
                'mensagem':'Pessoa não encontrada'
            }
            
        return response
    
    @auth.login_required()
    def put(self, name):
        
        pessoa = Pessoas.query.filter_by(name=name).first()
        
        dados = request.json
        
        if 'nome' in dados:
        
            pessoa.name = dados['nome']
        
        if 'idade' in dados:
        
            pessoa.age = dados['idade']
        
        pessoa.save()
        
        response = {
            'id' : pessoa.id,
            'nome' : pessoa.name,
            'idade' : pessoa.age
        }      
        
        return response

    @auth.login_required()
    def delete(self, name):
        
        pessoa = Pessoas.query.filter_by(name=name).first()
        pessoa.delete()
        
        response = {
            'status' : 'sucesso',
            'mensagem' : f'Pessoa {pessoa.name} excluida com sucesso.'
        }
        
        return response

class ListaPessoas(Resource):
    
    def get(self):
        
        pessoas = Pessoas.query.all()
        
        response = [{'id':i.id, 'nome':i.name, 'idade':i.age} for i in pessoas]
        
        return response

    @auth.login_required()
    def post(self):
        
        dados = request.json
        
        pessoa = Pessoas(name = dados['nome'], age = dados['idade'])
        
        pessoa.save()
        
        response = {
            'id' : pessoa.id,
            'nome' : pessoa.name,
            'idade' : pessoa.age
        }
        
        return response
    
class ListaAtividades(Resource):
    
    def get(self):
        
        atividades = Atividades.query.all()
        
        response = [{'id' : i.id, 'nome' : i.name, 'pessoa': i.pessoa.name} for i in atividades]
        
        return response
    
    @auth.login_required()
    def post(self):
        
        dados = request.json
        
        pessoa = Pessoas.query.filter_by(name= dados['pessoa']).first()
        
        atividade = Atividades(name = dados['nome'], pessoa = pessoa)
        
        atividade.save()
        
        response = {
            'pessoa' : atividade.pessoa.name,
            'nome' : atividade.name
        }
        
        return response
        
    
api.add_resource(Pessoa, '/pessoa/<string:nome>/')

api.add_resource(ListaPessoas, '/pessoas/')

api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug = True)