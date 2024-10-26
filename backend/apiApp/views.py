from django.shortcuts import render
from rest_framework import viewsets
from apiApp.models import Patient
from apiApp.serializers import PatientSerializer

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
