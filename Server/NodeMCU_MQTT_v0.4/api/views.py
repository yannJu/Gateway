from rest_framework import viewsets
from django.shortcuts import render
from .serializers import SensorSerializer, SecFileSerializer
from iot.models import Sensor, SecFile

# Create your views here.
# viewsets 는 serializer 를 통해 응답
# HTTP method 는 Model View Set 이 처리

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all().order_by('-id')
    serializer_class = SensorSerializer
    
class SecFileViewSet(viewsets.ModelViewSet):
    queryset = SecFile.objects.all().order_by('-id')
    serializer_class = SecFileSerializer