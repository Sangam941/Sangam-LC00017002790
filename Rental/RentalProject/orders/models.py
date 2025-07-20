from django.db import models
from booking.models import Booking

class Order(models.Model):
    STATUS = (
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('Co', 'Completed'),
    )
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS)

    def __str__(self):
        return f"Order for {self.booking.vehicle.name} by {self.booking.user.name}"
