# Blog Api

```bash
python -m venv .venv
. .venv/Scripts/activate

pip install django djangorestframework djangorestframework-simplejwt Pillow
pip freeze > requirements.txt

django-admin startproject blog
cd blog/
python manage.py startapp accounts

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```