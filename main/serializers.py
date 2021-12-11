from rest_framework import serializers
from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'created_at', 'updated_at']
