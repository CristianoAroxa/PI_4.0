from flask import Flask, render_template
from controllers import routes
from models.database import mongo, Aluna,Curso

app = Flask(__name__, template_folder='views')
routes.init_app(app)

# Definindo o endereço do MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/libby'

if __name__ == '__main__':
    mongo.init_app(app=app)
    # Adicionar um documento à coleção ao iniciar ao aplicativo
    with app.app_context():
        # Supondo que 'games' seja o nome da coleção
        if 'alunas' not in mongo.db.list_collection_names():
            # Insere um documento para criar a coleção
            aluna = Aluna(
                nome='',
                telefone='',
                email='',
                senha='',
                confirmaSenha=''
                
            )
            aluna.save()
        elif 'cursos' not in mongo.db.list_collections_names():
            curso = Curso(
                nome='',
                descricao='',
                valor='',
                cargaHoraria=''
            )
            curso.save()
    app.run(host='localhost', port=5000, debug=True) 