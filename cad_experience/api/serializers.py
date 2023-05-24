from rest_framework import serializers
from cad_experience.models import CadExperience

class CadExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CadExperience
        fields = ['cadexperience_id', 'cadexperience_first_name','cadexperience_last_name','cadexperience_degree']