from database import db
from flask_login import UserMixin #Importa os metodos de Autenticacao

#Colunas: id (int), username (text), password (text)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #Declaracao de tipo
    username = db.Column(db.String(80), nullable=False, unique=True) #nullable = False - Obriga usuario a nao deixar nulo
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='user')
