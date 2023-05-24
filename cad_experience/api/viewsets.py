from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, authentication
from .serializers import CadExperienceSerializer
from cad_experience.models import CadExperience

class CadExperienceSet(viewsets.ModelViewSet):
    queryset = CadExperience.objects.all()
    serializer_class = CadExperienceSerializer
    