
from django.urls import path
from . import views

urlpatterns = [
    # FBV
    # path('fbv/todos/', views.todo_list),
    # path('fbv/todos/<int:pk>/', views.todo_detail),

    # CBV
    path('cbv/todos/', views.TodoList.as_view()),
    path('cbv/todos/<int:pk>/', views.TodoDetail.as_view()),
]
