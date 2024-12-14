from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# conexão com banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresaula:PostgresAula123!@postgres-aula.cuebxlhckhcy.us-east-1.rds.amazonaws.com:5432/postgresaula'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Criação do objeto SQLAlchemy
db = SQLAlchemy(app)

# Definindo o modelo de exemplo para a tabela 'contatos'
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class Cliente(db.Model):
    __tablename__ = 'cliente_murilo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Endpoint para processar o envio do formulário
@app.route('/enviar', methods=['POST'])
def enviar():
    # Captura os dados enviados no formulário
    nome = request.form['nome']
    email = request.form['email']
    
    # Salva os dados no banco de dados
    novo_contato = Contato(nome=nome, email=email)
    db.session.add(novo_contato)
    db.session.commit()

    # Retorna uma resposta para o usuário
    return render_template('sucesso.html', nome=nome, email=email)  

# Criando as tabelas no banco de dados (executar apenas uma vez no início)
with app.app_context():
    db.create_all()

@app.route('/')
def menu():    
   return render_template('menu.html')

@app.route('/aila.html')
def aila():
    return render_template('aila.html')

@app.route('/witcher.html')
def witcher():
    return render_template('witcher.html')

@app.route('/cod.html')
def cod():
    return render_template('cod.html')

@app.route('/cyberpunk.html')
def cyberpunk():
    return render_template('cyberpunk.html')

@app.route('/fobia.html')
def fobia():
    return render_template('fobia.html')

@app.route('/rd2.html')
def rd2():
    return render_template('rd2.html')

@app.route('/re4.html')
def re4():
    return render_template('re4.html')

@app.route('/ajuda.html')
def ajuda():
    return render_template('ajuda.html')

if __name__ == '__main__':
    app.run(debug=True)
