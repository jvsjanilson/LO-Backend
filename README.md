## API - Livraria Online - DB MySQL

## Instruções para instalação

1. Clone o projeto

    **git clone git@github.com:jvsjanilson/lo-backend.git**

2. No diretorio do projeto crie o ambiente virtual

    **python -n venv .venv**
   
    **source .venv/Scripts/activate**

4. Instale as dependências do projeto

    **pip install -r requirements.txt**
   
6. Crie um banco de dados chamado db_livraria no MySQL
   
   **Verificar configuracções no arquivo setup/settings.py**

8. Rodar as makemigrations

    **python manage.py makemigrations core compra**

9. Rodar a migrate

    **python manage.py migrate**

10. Para rodar a aplicação

    **python manage.py runserver 0.0.0.0:80**
