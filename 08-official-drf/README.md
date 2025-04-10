# Official Django REST_FRAMEWORK Tutorial

## A simple pastebin code highlighting Web API.

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install djangorestframework pygments
django-admin startproject tutorial
python manage.py startapp snippets

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```