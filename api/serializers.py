from rest_framework import serializers
from .models import Appels

class ApelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appels
        fields = '__all__'
