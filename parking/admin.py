from django.contrib import admin
from .models import ParkingLot, VehicleType, ParkingSpot, Vehicle, ParkingTicket

admin.site.register(ParkingLot)
admin.site.register(VehicleType)
admin.site.register(ParkingSpot)
admin.site.register(Vehicle)
admin.site.register(ParkingTicket)
