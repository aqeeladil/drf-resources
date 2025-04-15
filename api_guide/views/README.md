# Views

- **Function-Based Views (FBVs) – using @api_view**

    - FBVs are simple Python functions that handle HTTP requests. In Django REST Framework, we use the @api_view decorator to convert a regular Django view into a REST API view.

- **Class-Based Views (CBVs) – using APIView**

    - CBVs use object-oriented programming (OOP). You subclass APIView and implement methods like .get(), .post(), etc.

## Comparison

FBV: User List & Create
```python
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        usernames = [user.username for user in users]
        return Response(usernames)
    
    if request.method == 'POST':
        username = request.data.get('username')
        if not username:
            return Response({"error": "Username required"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(username=username)
        return Response({"message": f"User {user.username} created"}, status=status.HTTP_201_CREATED)
```

CBV: User List & Create
```python
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        usernames = [user.username for user in users]
        return Response(usernames)
    
    def post(self, request):
        username = request.data.get('username')
        if not username:
            return Response({"error": "Username required"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(username=username)
        return Response({"message": f"User {user.username} created"}, status=status.HTTP_201_CREATED)
```

## Authentication, Permissions, and Throttling

In CBVs, you define these as class attributes:
```python
from rest_framework import authentication, permissions

class AdminOnlyView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        return Response({"message": "You are an admin!"})
```

In FBVs, you use decorators:
```python
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAdminUser])
def admin_view(request):
    return Response({"message": "You are an admin!"})
```

## Demo Project

A simple To-Do API using both Function-Based Views (FBV) and Class-Based Views (CBV) with Django REST Framework.

```bash
django-admin startproject to_do .
python manage.py startapp api
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```