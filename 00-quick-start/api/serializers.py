from django.contrib.auth.models import User, Group
from rest_framework import serializers


class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        extra_kwargs = {
            'url': {'view_name': 'user-detail'},
            'groups': {'view_name': 'group-list'}
        }

class Groupserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'group-detail'}
        }

