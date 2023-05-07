from rest_framework import serializers
from gateway.models import SecFile

class SecFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecFile
        fields = ('file_name', 'sec_file')