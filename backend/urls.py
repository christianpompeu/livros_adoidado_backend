from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', admin.site.urls, name='index'),
    # path('api_auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls, name='admin'),
]
