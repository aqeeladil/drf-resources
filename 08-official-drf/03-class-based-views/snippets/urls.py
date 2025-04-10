from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns     # 

urlpatterns = [
    # path('snippets/', views.snippet_list),
    path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
'''
this will add the suffixes to the URLs. for example, if you have a URL like /snippets/1.json, it will return the 
JSON representation of the snippet with ID 1. If you have a URL like /snippets/1.xml, it will return the 
XML representation of the snippet with ID 1. This is useful for APIs that need to support multiple formats.

'''
