from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('users/create/', views.create_user, name='create_user'),
#     path('users/<int:pk>/', views.update_user, name='update_user'),
#     path('users/<int:pk>/delete/', views.delete_user, name='delete_user'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
]

# ]
