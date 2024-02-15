from flask import Flask

from flask import jsonify

from flask import request

import json

app = Flask(__name__)

dev_list = [
    {'id':'0','nome':'Victor', 'habilidades':['Python', 'Flask']},
    {'id':'1','nome':'Lucas', 'habilidades':['Python', 'Django']}
]

# devolve um desenvolvedor pelo id, também inclui e deleta um desenvolvedor pelo id
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    
    if request.method == 'GET':

        try:
    
            response  = dev_list[id]

        except IndexError:
            
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            
            response = {'status':'erro', 'mensagem':mensagem}

        except Exception:
            
            mensagem = f'Erro desconhecido. Contate o administrador da API.'
            
            response = {'status':'erro', 'mensagem':mensagem}
            
        return jsonify(response)
    
    elif request.method == 'PUT':
        
        data = json.loads(request.data)

        dev_list[id] = data
        
        return jsonify(data)
    
    elif request.method == 'DELETE':
        
        dev_list.pop(id)
        
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído.'})

@app.route('/dev/', methods = ['POST', 'GET'])
def list_devs():

    if request.method == 'POST':

        data = json.loads(request.data)
        
        index = len(dev_list)
        
        data['id'] = index 

        dev_list.append(data)
        
        return jsonify(dev_list[index])
    
    if request.method == 'GET':
        return jsonify(dev_list)

if __name__ == "__main__":
    app.run()