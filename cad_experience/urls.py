from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import CadExperienceSet

router = routers.DefaultRouter()
router.register(r'cad_experience', CadExperienceSet)

urlpatterns = [
    path('', include(router.urls))
]
