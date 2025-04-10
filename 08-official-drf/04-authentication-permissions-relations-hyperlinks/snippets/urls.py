from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns     # 

urlpatterns = [ 
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root, name='api-root'),  # this will be the root URL of the API
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
'''
this will add the suffixes to the URLs. for example, if you have a URL like /snippets/1.json, it will return the 
JSON representation of the snippet with ID 1. If you have a URL like /snippets/1.xml, it will return the 
XML representation of the snippet with ID 1. This is useful for APIs that need to support multiple formats.

'''
