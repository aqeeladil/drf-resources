from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# List all tasks or create a new one
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Retrieve, update, or delete a specific task
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
