from django.db import models
from django.utils import timezone


class ParkingLot(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.address})"


class VehicleType(models.Model):
    type_name = models.CharField(max_length=20)  # Example: Car, Bike, Truck

    def __str__(self):
        return self.type_name


class ParkingSpot(models.Model):
    spot_number = models.CharField(max_length=10)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Spot {self.spot_number} ({self.vehicle_type}) in {self.lot.name}"


class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=100)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicle_number} - {self.owner_name}"


class ParkingTicket(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(default=timezone.now)
    exit_time = models.DateTimeField(null=True, blank=True)
    fee_charged = models.FloatField(null=True, blank=True)

    def exit(self):
        self.exit_time = timezone.now()
        self.spot.is_occupied = False
        self.spot.save()
        self.fee_charged = self.calculate_fee()
        self.save()

    def calculate_fee(self):
        base_fees = {
            'Car': 20,
            'Bike': 10,
            'Truck': 30,
        }
        if not self.exit_time:
            return 0
        duration = self.exit_time - self.entry_time
        hours = max(1, int(duration.total_seconds() // 3600))
        return base_fees.get(self.vehicle.vehicle_type.type_name, 20) * hours

    def __str__(self):
        return f"[{self.vehicle.vehicle_number}] at {self.spot.spot_number} | In: {self.entry_time}, Out: {self.exit_time}, Fee: ₹{self.fee_charged}"
