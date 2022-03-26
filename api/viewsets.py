from rest_framework import viewsets, generics

from api.serializers import TaskSerializer
from todo.models import Task


class TaskCreateSet(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListSet(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateSet(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteSet(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
