from rest_framework import serializers
from .models import Payment

class PaymentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['booking','payment_method','payment_date','amount','paid']