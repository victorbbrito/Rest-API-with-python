from flask import request

from flask_restful import Resource

import json

skills_list = ['Python', 'Java', 'PHP', 'C', 'C++', 'C#', 'JavaScript']

class Habilidades(Resource):
    
    def get(self):
        
        return skills_list
    
    def put(self, id):
        data = json.loads(request.data)

        skills_list[id] = data
        
        return skills_list
    
    def post(self):
        
        data = json.loads(request.data)
        
        index = len(skills_list)
        
        data['id'] = index 

        skills_list.append(data)
        
        return skills_list
    
    def delete(self, id):

        skills_list.pop(id)
        
        return skills_list
    
    
        