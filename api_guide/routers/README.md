# Routers

Routers automatically generate URLs for your API based on your viewsets. Instead of manually writing a URL pattern for each API action (list, create, retrieve, etc.), routers handle this for you.

## Demo

```bash
django-admin startproject drf_router_demo .
python manage.py startapp api

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```