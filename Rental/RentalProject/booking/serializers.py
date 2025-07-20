from rest_framework import serializers
from .models import Booking

class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user','vehicle','start_date','end_date','total_price','booked_on']