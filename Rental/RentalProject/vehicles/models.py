from django.db import models

# Create your models here.

class Vehicles(models.Model):
    VEHICLE_TYPE = (
        ('car', 'Car'),
        ('van', 'van'),
        ('bike', 'Bike'),
    )
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_Available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_type}"