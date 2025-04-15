from django.urls import path
from . import views

urlpatterns = [
    path('anonymous/', views.AnonymousView.as_view()),
    path('user/', views.UserView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('upload/', views.UploadView.as_view()),
    path('random/', views.RandomThrottleView.as_view()),
]
