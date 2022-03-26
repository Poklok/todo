from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('accounts/', include('register.urls')),
    path('api/',include('api.urls')),
    path('', include('social_django.urls')),
]
