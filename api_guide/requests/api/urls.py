from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.list_notes),
    path('notes/create/', views.create_note),
]
