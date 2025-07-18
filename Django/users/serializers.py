from rest_framework import serializers
from .models import Users

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id","name", "age", "email", "bio", "password"]

        exta_kwargs = {
            'password': {'write_only' : True},
            'email' : {'required' : True},
        }

    def get_full_info(self, obj):
        return f"{obj.name} ({obj.email})"
    
    def validate(self, data):
        if data['user'].toLower() == data['email'].split('@')[0].lower():
            raise serializers.ValidationError("Name and email should not be same")
        return data
    
    def validate_age(self, value):
        if value < 10:
            raise serializers.ValidationError("Age must be grater than 10")
        return value
    
    def create(self, validate_date):
        return Users.objects.create(**validate_date)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance