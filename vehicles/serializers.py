from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Car, Truck, Boat


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year',
                    'seats', 'color', 'vin', 'current_mileage',
                    'service_interval', 'next_service')


class TruckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Truck
        fields = ('id', 'make', 'model', 'year',
                    'seats', 'bed_length', 'color', 'vin',
                    'current_mileage', 'service_interval', 'next_service')


class BoatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boat
        fields = ('id', 'make', 'model', 'year',
                    'length', 'width', 'hin', 'current_hours',
                    'service_interval', 'next_service')

