from rest_framework import serializers
from .models import Vehicles

class VehicleSerializer (serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['name', 'vehicle-type', 'price', 'is_Available']