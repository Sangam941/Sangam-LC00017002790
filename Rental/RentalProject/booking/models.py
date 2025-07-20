from django.db import models
from users.models import Users
from vehicles.models import Vehicles

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.vehicle.name}"