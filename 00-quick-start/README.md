## Quickstart

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install djangorestframework
django-admin startproject tutorial .
django-admin startapp quickstart

python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com

python manage.py runserver
```