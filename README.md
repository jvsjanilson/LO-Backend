## API - Livraria Online

## Instruções para instalação

1. Clone o projeto

    **git clone git@github.com:jvsjanilson/lo-backend.git**

2. No diretorio do projeto crie o ambiente virtual

    **python3 -n venv .venv**

3. Instale as dependências do projeto

    **pip3 install -r requirements.txt**

4. Rodar as makemigrations

    **python3 manage.py makemigrations core compra**

5. Rodar a migrate

    **python3 manage.py migrate**

6. Para rodar a aplicação

    **python3 manage.py runserver 0.0.0.0:80**
