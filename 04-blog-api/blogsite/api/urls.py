from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-list'),
    path('blogposts/<int:pk>/', views.BlogPostDetail.as_view(), name='blogpost-detail'),
    # path('blogposts/<int:pk>/delete/', views.BlogPostDetail.as_view(), name='blogpost-delete'),
]
