## Django REST API

```bash
python -m venv .my_env1
source .my_env3/Scripts/activate

pip install djangorestframework
pip freeze > requirements.txt

django-admin startproject newproject .
python manage.py startapp api

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

Visit these endpoints
- `localhost:8000/admin/`
- `localhost:8000/api/users/`
- `localhost:8000/api/users/create/`
- `localhost:8000/api/users/1`


