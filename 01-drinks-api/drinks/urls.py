"""
URL configuration for drinks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', views.drink_list),
    path('drinks/<int:id>', views.drink_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)   # this is needed for the browsable API. For example, if you go to localhost:8000/drinks/1.json, you will get the JSON representation of the drink with id=1. If you go to localhost:8000/drinks/1.html, you will get the HTML representation of the drink with id=1. 