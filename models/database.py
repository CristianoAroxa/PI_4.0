from flask_pymongo import PyMongo
from bson import ObjectId

mongo = PyMongo

class Aluna():
    def __init__(self, nome, telefone, email, senha, confirmaSenha):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.confirmaSenha = confirmaSenha
    
    def salvar(self):
        mongo.db.alunas.insert_one({
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
           'senha': self.senha,
            'confirmaSenha': self.confirmaSenha
        })

    @staticmethod
    def get_all():
        return list(mongo.db.alunas.find())
    
    @staticmethod
    def get_by_id(id):
        return mongo.db.alunas.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def get_by_email(email):
        return mongo.db.alunas.find_one({'email': email})
    
    @staticmethod
    def delete(id):
        mongo.db.alunas.delete_one({'_id': ObjectId(id)})

    def update(self, id):
        mongo.db.alunas.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'nome': self.nome,
                'telefone': self.telefone,
                'email': self.email,
               'senha': self.senha,
                'confirmaSenha': self.confirmaSenha
            }}
        )

class Curso():
    def __init__(self, nome, descricao, valor, cargaHoraria):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.cargaHoraria = cargaHoraria
    
    def salvarCurso(self):
        mongo.db.cursos.insert_one({
            'nome': self.nome,
            'descricao': self.descricao,
            'valor': self.valor,
            'cargaHoraria': self.cargaHoraria
        })
    
    @staticmethod
    def get_all_curso():
        return list(mongo.db.cursos.find())
    
    @staticmethod
    def get_by_id_curso(id):
        return mongo.db.cursos.find_one({'_id': ObjectId(id)})
    
    @staticmethod
    def delete_curso(id):
        mongo.db.cursos.delete_one({'_id': ObjectId(id)})
    
    @staticmethod
    def update_curso(self,id):
        mongo.db.cursos.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'nome': self.nome,
                'descricao': self.descricao,
                'valor': self.valor,
                'cargaHoraria': self.cargaHoraria
            }}
        )   

    
        

        
