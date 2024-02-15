from flask import Flask
from flask import jsonify
from flask import request

import json

task_list= [
    {'id':'0', 'responsavel':'Victor', 'tarefa':'Desenvolver a API', 'status':'In Progress'},
    {'id':'1', 'responsavel':'Fabio', 'tarefa':'Desenvolver um RPA', 'status':'In Progress'},
    {'id':'2', 'responsavel':'Rafael', 'tarefa':'Desenvolver um design', 'status':'Done'},
    {'id':'3', 'responsavel':'Lucas', 'tarefa':'Desenvolver um RPA', 'status':'In Progress'}
]

app = Flask(__name__)

@app.route('/task/<int:id>/', methods = ['GET', 'PUT', 'DELETE'])
def task_by_id(id):

    if request.method == 'GET':

        try:
    
            response = task_list[id]
    
        except IndexError:
    
            mensage = f"A tarefa com ID {id} não foi encontrada."
    
            response = jsonify({'status':'error', 'mensagem':mensage})
    
        except Exception:
    
            mensagem = f'Erro desconhecido. Contate o administrador da API.'
            
            response = {'status':'erro', 'mensagem':mensagem}
    
        return jsonify(response)
    
    elif request.method == 'PUT':
        
        data = json.loads(request.data)

        task_list[id]['status'] = data['status']
        
        return jsonify(task_list[id])
    
    elif request.method == 'DELETE':
        
        task_list.pop(id)
        
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído.'})
    
@app.route('/tasks/', methods = ['GET', 'POST'])
def list_tasks():

    if request.method == 'GET':

        return jsonify(task_list)
    
    elif request.method == 'POST':
        data = json.loads(request.data)
        
        index = len(task_list)
        
        data['id'] = index 

        task_list.append(data)
        
        return jsonify(task_list[index])


if __name__ == '__main__':
    app.run()