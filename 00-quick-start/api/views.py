from django.contrib.auth.models import User, Group
from .serializers import Userserializer, Groupserializer
from rest_framework import viewsets, permissions


class UserViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = Userserializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = Groupserializer
    permission_classes = [permissions.IsAuthenticated]