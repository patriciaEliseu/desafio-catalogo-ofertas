# 📦 Catálogo de Ofertas

Este desafio coleta ofertas do Mercado Livre usando Selenium e exibe os produtos em uma página web feita com Django. 


## 🛠 Tecnologias Utilizadas
- Python 
- Django
- Selenium
- PostgreeSQL 

## 📥 Preparar Ambiente de Desenvolvimento:
```sh
1. Verificar versão do python;
   comandos:
      python3 --version
2. Criar pasta do desafio e entrar na sua pasta;
   comandos:
      mkdir desafio-catalogo-ofertas &&
      cd desafio-catalogo-ofertas
3. Criar e ativar ambiente virtual (venv);
   comandos:
      python3 -m venv .venv &&
      source .venv/bin/activate
4. Iniciar o git para poder criar conexão com o github;
   comandos:
      git init
5. Criei o arquivo .gitignore;
   para ignorar .venv etc...

  
```

## 📥  Fazer configuração do BD PostgreSql;
```sh
1. Instalar o Postgre;
   comandos:
      sudo apt install postgresql postgresql
2. Entrei no postgresql;
   comandos:
      sudo -u postgres psql;
2. Crei usuario e senha do postgres;
   comandos:
      CREATE USER novo_usuario WITH PASSWORD 'sua_senha' &&
      ALTER USER root WITH PASSWORD 'nova_senha'
3. Fiz o start do postgresql;
   comandos:
      sudo systemctl restart postgresql
4. Dei permissão para o meu usuario na minha database;
   comandos:
      GRANT ALL PRIVILEGES ON DATABASE catalogoofertasdatabase TO novo_usuario
5. Criei o banco de dados catalogoofertasdatabase;
   comandos:
      CREATE DATABASE catalogoofertasdatabase
6. Configurei o arquivo catalogos_ofertas/settings.py
   
      DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.postgresql',
               'NAME': 'catalogoofertasdatabase',
               'USER': 'seu_usuario',
               'PASSWORD': 'sua_senha',
                'HOST': '127.0.0.1',
               'PORT': '5432',
            }
      }
```
### 📌 Para executar o projeto
 
      python3 manage.py runserver

### 📌 Aplicar as MIgrations

      python3 manage.py migrate

### 📌 Instalar o driver do Chrome(webDriver)

      pip install webdriver-manager

### 📌 Criar senha de superusuario para o Template

