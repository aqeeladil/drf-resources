from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers
from django.contrib.auth.models import User



# class SnippetSerializer(serializers.ModelSerializer):
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')


    class Meta:
        model = Snippet
        # fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
        fields = ('url', 'id', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')
        


# class UserSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


