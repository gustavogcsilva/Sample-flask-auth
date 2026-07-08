from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Configuração da chave secreta para sessões e segurança
app.config['SECRET_KEY'] = 'your_secret_key'
#Caminho obrigatório para o banco de dados SQLite
app.config['SQLAlchemy_DATABASE_URI'] = 'sqllite:///database.db'



db = SQLAlchemy(app)

@app.route("/Hello-World", methods=['GET'])
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)