from rest_framework import serializers
from .models import ParkingLot, VehicleType, ParkingSpot, Vehicle, ParkingTicket

class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ParkingTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingTicket
        fields = '__all__'
