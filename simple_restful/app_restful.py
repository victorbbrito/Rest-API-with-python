from flask import Flask, request

from flask_restful import Resource, Api

import json

from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

dev_list = [
    {'id':0,'nome':'Victor', 'habilidades':Habilidades},
    {'id':1,'nome':'Lucas', 'habilidades':Habilidades},
    {'id':2,'nome':'Lucas', 'habilidades':Habilidades}
]

class Desenvolvedor(Resource):
    
    def get(self, id):
        try:
        
            response  = dev_list[id]

        except IndexError:
                
            mensagem = f'Desenvolvedor de ID {id} não existe.'
                
            response = {'status':'erro', 'mensagem':mensagem}

        except Exception:
                
            mensagem = f'Erro desconhecido. Contate o administrador da API.'
                
            response = {'status':'erro', 'mensagem':mensagem}
                
        return response
    
    def put(self, id):
        
        data = json.loads(request.data)

        dev_list[id] = data
        
        return data
    
    def delete(self, id):
        
        dev_list.pop(id)
        
        return {'status':'sucesso', 'mensagem':'Registro excluído.'}
       
       
class ListaDesenvolvedores(Resource):
    
    def get(self):
        
        return dev_list
    
    def post(self):
        
        data = json.loads(request.data)
        
        index = len(dev_list)
        
        data['id'] = index 

        dev_list.append(data)
        
        return dev_list[index]
    
    
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')


if __name__ == '__main__':
    app.run()