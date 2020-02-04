from django.contrib.auth import views as auth_views
from django.urls import path,re_path,include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "apps.tution"
router = DefaultRouter()
router.register(r'', TutionViewSet,basename="tution")

urlpatterns = [
    path('', include(router.urls)),
]