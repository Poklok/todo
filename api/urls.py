from django.urls import path, include
from rest_framework import routers

from api.viewsets import TaskListSet, TaskCreateSet, TaskUpdateSet, TaskDeleteSet

urlpatterns = [
    path('v1', TaskListSet.as_view()),
    path('v1/create', TaskCreateSet.as_view()),
    path('v1/<int:pk>', TaskUpdateSet.as_view()),
    path('v1/<int:pk>/delete', TaskDeleteSet.as_view())

]
