from rest_framework import serializers
from gateway.models import DetectFile

class DetectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectFile
        fields = ('file_name', 'sec_file')