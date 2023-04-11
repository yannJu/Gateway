from django.db import models

# Create your models here.
class Sensor(models.Model):
    place = models.CharField(max_length=50) # Sensor 설치 장소
    category = models.CharField(max_length=50) # Sensor 종류
    value = models.FloatField() # Sensor 값
    created_at = models.DateTimeField() # Sensor 측정 날짜 - 시간