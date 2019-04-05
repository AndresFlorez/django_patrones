from exp_framework_lab.apps.personas.models import Persona
from rest_framework import serializers


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombres', 'apellidos', 'edad')