from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<uuid:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('public-blog/', views.PublicBlogView.as_view(), name='public_blog'),
]