from rest_framework import viewsets
from django.shortcuts import render
from .serializers import DetectFileSerializer
from gateway.models import DetectFile

# Create your views here.

class DetectFileViewSet(viewsets.ModelViewSet):
    queryset = DetectFile.objects.all().order_by('-id')
    serializer_class = DetectFileSerializer