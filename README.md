# Flask Authentication API

API de autenticação desenvolvida em Flask com persistência de dados em MySQL e criptografia de senhas.

## 🚀 Tecnologias

- **Flask**: Framework web Python para desenvolvimento da API
- **MySQL**: Banco de dados relacional para persistência dos dados
- **SQLAlchemy**: ORM para interação com o banco de dados
- **Flask-Login**: Gerenciamento de sessões e autenticação
- **Docker & Docker Compose**: Containerização e orquestração
- **Bcrypt**: Criptografia de senhas

## 📋 Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.8 ou superior
- Git

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/guburchardt/sample_flask_auth.git
cd sample_flask_auth
```

2. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```
Edite o arquivo `.env` com suas configurações.

3. Inicie os containers:
```bash
docker-compose up -d
```

4. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

5. Inicialize o banco de dados:
```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

6. Inicie a aplicação:
```bash
python app.py
```

## 📚 Documentação da API

### Endpoints

#### Autenticação
- `POST /login`: Login de usuário
- `GET /logout`: Logout de usuário

#### Usuários
- `POST /user`: Criação de usuário
- `GET /user/<id>`: Consulta de usuário
- `PUT /user/<id>`: Atualização de usuário

### Exemplos de Requisições

#### Login
```json
POST /login
{
    "username": "usuario",
    "password": "senha123"
}
```

#### Criação de Usuário
```json
POST /user
{
    "username": "novo_usuario",
    "password": "senha123"
}
```

#### Atualização de Usuário
```json
PUT /user/1
{
    "password": "nova_senha"
}
```

### Respostas da API

#### Login Bem-sucedido
```json
{
    "message": "Autenticacao realizada com sucesso"
}
```

#### Login Falho
```json
{
    "message": "Credenciais inválidas"
}
```

#### Criação de Usuário Bem-sucedida
```json
{
    "message": "Usuário cadastrado com sucesso"
}
```

#### Criação de Usuário Falha
```json
{
    "message": "Dados inválidos"
}
```

#### Consulta de Usuário Bem-sucedida
```json
{
    "username": "nome_do_usuario"
}
```

#### Consulta de Usuário Falha
```json
{
    "message": "Usuário nao encontrado"
}
```

#### Atualização de Usuário Bem-sucedida
```json
{
    "message": "Usuário 1 atualizado com sucesso"
}
```

#### Atualização de Usuário Falha
```json
{
    "message": "Usuário nao encontrado"
}
```

## 🔒 Segurança

- Senhas são criptografadas usando Bcrypt
- Rotas protegidas com autenticação via token
- Validação de dados de entrada
- Proteção contra SQL Injection através do SQLAlchemy

## 🛠️ Estrutura do Projeto

```
sample_flask_auth/
├── app.py              # Aplicação principal
├── models/             # Modelos do banco de dados
│   └── user.py         # Modelo de usuário
├── database.py         # Configuração do banco de dados
├── requirements.txt    # Dependências Python
├── docker-compose.yml  # Configuração Docker
└── .env.example        # Exemplo de variáveis de ambiente
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📫 Contato

Gustavo Burchardt - [@guburchardt](https://github.com/guburchardt)


 