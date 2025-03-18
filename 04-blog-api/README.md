# Blog Api

```bash
python -m venv .venv
. .venv/Scripts/activate

pip install djangorestframework
pip freeze > requirements.txt

django-admin startproject blogsite
cd blogsite/
python manage.py startapp api

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```