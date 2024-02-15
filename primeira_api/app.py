import json

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route("/<int:id>")
def pessoas(id):
    return jsonify({'id':id,'nome':'Rafael'})


@app.route('/soma', methods=['POST', 'PUT', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
        return jsonify({'soma': total})
    
    elif request.method == 'GET':
        total = 10+10
        return jsonify({'soma': total})


if __name__ == "__main__":
    app.run(debug = True)