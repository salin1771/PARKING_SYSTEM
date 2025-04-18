from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'lots', ParkingLotViewSet)
router.register(r'vehicle-types', VehicleTypeViewSet)
router.register(r'spots', ParkingSpotViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'tickets', ParkingTicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
