from rest_framework import serializers
from ..models import *

class CarSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ['car_model', 'car_year', 'car_type', 'car_bodytype', 'car_engine']
