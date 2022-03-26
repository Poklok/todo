
from rest_framework import viewsets

from api.serializers import TaskSerializer
from todo.models import Task


class TaskListSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer