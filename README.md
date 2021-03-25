# django-rest-app

A Django project with a lot of DRF (Django Rest Framework) on it.

Como executar o projeto:

1. Caso não tenha o pipenv instalado:
```console
pip install pipenv
pipenv sync -d
```

2. Caso tenha o pipenv instalado:
```console
pipenv sync -d
```

3. Crie o arquivo .env e dentro deste crie as seguintes variáveis de ambiente:
- DEBUG=True
- ALLOWED_HOSTS=localhost,127.0.0.1
- SECRET_KEY=minhachave

4. Faça a migração dos dados do projeto digitando os seguintes comandos:
```console
pipenv run python manage.py makemigrations

pipenv run python manage.py migrate
```

5. Crie um superusuário:
```console
pipenv run python manage.py createsuperuser
```

6. Rode o servidor:
```console
pipenv run python manage.py runserver
```

7. Entre no admin:
- http://127.0.0.1:8000/admin/

8. Use o projeto.
