from django.urls import path, include
from rest_framework import routers

from api.viewsets import TaskListSet

router = routers.DefaultRouter()
router.register(r'task', TaskListSet)

urlpatterns = [
    path('', include(router.urls), name='v1')
]
