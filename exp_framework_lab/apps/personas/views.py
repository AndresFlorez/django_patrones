from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from exp_framework_lab.apps.personas.models import Persona
from exp_framework_lab.apps.personas.serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
