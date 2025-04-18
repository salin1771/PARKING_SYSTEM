from rest_framework import viewsets
from .models import ParkingLot, VehicleType, ParkingSpot, Vehicle, ParkingTicket
from .serializers import *

class ParkingLotViewSet(viewsets.ModelViewSet):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer

class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class ParkingTicketViewSet(viewsets.ModelViewSet):
    queryset = ParkingTicket.objects.all()
    serializer_class = ParkingTicketSerializer
