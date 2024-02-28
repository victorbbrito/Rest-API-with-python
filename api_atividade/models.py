from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session

from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy import ForeignKey

from sqlalchemy import Boolean

engine = create_engine("sqlite:///atividades.db")
db_session = scoped_session(sessionmaker(autocommit = False, bind = engine))

base = declarative_base()
base.query = db_session.query_property()

class Pessoas(base):
    
    __tablename__ = 'pessoas'
    
    id = Column(Integer, primary_key = True)
    
    name = Column(String(40), index = True)
    
    age = Column(Integer) 
    
    
    def __repr__(self):
    
        return '<Pessoa {}>'.format(self.name)
    
    
    def __str__(self):
    
        return str(self.id)+"\n"+self.name+"\n"+str(self.age)
    
    
    def save(self):
    
        db_session.add(self)
    
        db_session.commit()  
    
        
    def delete(self):
    
        db_session.delete(self)
    
        db_session.commit()      


class Atividades(base):

    __tablename__ = 'atividades'

    id = Column(Integer, primary_key = True)

    name = Column(String(80))

    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))

    pessoa = relationship("Pessoas")
    
    
    def save(self):
    
        db_session.add(self)
    
        db_session.commit()  
    
        
    def delete(self):
    
        db_session.delete(self)
    
        db_session.commit()  

    
class Usuarios(base):

    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key = True)

    login = Column(String(20), unique= True)

    password = Column(String(20))
    
    status = Column(Boolean(True))

    def __repr__(self):
        
        return '<Usuario {}>'.format(self.login)
    
    
    def save(self):
        
        db_session.add(self)
        
        db_session.commit()
        
    
    def delete(self):
        
        db_session.delete(self)
        
        db_session.commit()


def init_db():
    base.metadata.create_all(bind = engine)
    
if __name__ == '__main__':
    init_db()
    