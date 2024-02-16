from models import Pessoas

def insere_pessoas():
    
    pessoa = Pessoas(name= 'Victor', age=29)
    
    pessoa.save()
    
def consulta_pessoa():
    
    pessoa = Pessoas.query.filter_by(name = 'Rafael').first()
    
    print(pessoa)

def altera_pessoa():
    
    pessoa = Pessoas.query.filter_by(name = 'Rafael').first()
    
    pessoa.age = 22
    
    pessoa.save()
    
    print(pessoa)

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(name= 'Rafael').first()
    pessoa.delete()
    
if __name__ == "__main__":
    insere_pessoas()
    consulta_pessoa()
    altera_pessoa()
    exclui_pessoa()
    consulta_pessoa()