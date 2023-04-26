# form 클래스 역할과 유사
# form 이 아닌 json 으로 한다는 점이 다르다
# model 을 기반으로 타입, 제약조건 명시

from rest_framework import serializers
from iot.models import Sensor, SecFile

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'place', 'category', 'value', 'created_at') # 직렬화에 포함시킬 value (필요업는건 생략 가능)
    
class SecFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecFile
        fields = ('file_name', 'sec_file')