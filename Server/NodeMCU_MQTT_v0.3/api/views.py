from rest_framework import viewsets
from django.shortcuts import render
from .serializers import SecFileSerializer
from gateway.models import SecFile

# Create your views here.

class SecFileViewSet(viewsets.ModelViewSet):
    queryset = SecFile.objects.all().order_by('id')
    serializer_class = SecFileSerializer