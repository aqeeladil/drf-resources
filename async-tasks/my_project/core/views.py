from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
