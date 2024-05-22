from flask import render_template, request, url_for, redirect
from models.database import Aluna, Curso
import urllib

alunaList = []
cursoList =[]

def init_app(app):

    @app.route('/')
    def home():        
        return render_template('home.html')
    
    @app.route('/alunas', methods=['GET', 'POST'])
    def alunas():       
        if request.method == 'GET':
            alunas = Aluna.query.all()
            return render_template('alunas.html', alunas=alunas)
        elif request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            telefone = request.form['telefone']
            aluna = Aluna(nome, email, telefone)
            aluna.save()
            return redirect(url_for('alunas'))
    
    @app.route('/cadAluna', methods=['GET', 'POST'])
    def cadAluna():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('telefone') and request.form.get('email') and request.form.get('senha') and request.form.get('confirmaSenha'):
                alunaList.append({'Nome' : request.form.get('nome'), 'Email' : request.form.get('nome'), 'Telefone' : request.form.get('telefone'), 'E-mail' : request.form.get('email'), 'Senha' : request.form.get('senha'), 'Confirma Senha' : request.form.get('confirmaSenha')})

        return render_template('cadAluna.html', alunaList=alunaList) 
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            aluna = Aluna.query.filter_by(email=email, senha=senha).first()
            if aluna is not None:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
            
    @app.route('/logout')
    def logout():
        return redirect(url_for('home'))
    
    @app.route('/video')
    def video():
        return render_template('video.html')
    
    @app.route('/cursos')
    def cursos():
        if request.method == 'GET':
            cursos = Curso.query.all()
            return render_template('cursos.html', cursos=cursos)
        elif request.method == 'POST':
            nome = request.form['nome']
            descricao = request.form['descricao']
            valor = request.form['valor']
            cargaHoraria = request.form['cargaHoraria']
            curso = Curso(nome, descricao, valor, cargaHoraria)
            curso.save()
            return redirect(url_for('cursos'))       
    
    @app.route('cadCurso')
    def cadCurso():  
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('descricao') and request.form.get('valor') and request.form.get('cargaHoraria'):
                cursoList.append({'Nome' : request.form.get('nome'), 'Descrição' : request.form.get('descricao'), 'Valor' : request.form.get('valor'), 'Carga Horária' : request.form.get('cargaHoraria')})

        return render_template('cadCurso.html', cursoList=cursoList)
           
        



    
        