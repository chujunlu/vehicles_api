from django.contrib.auth.models import User
from rest_framework import generics

from .models import Car, Truck, Boat
from .serializers import (CarSerializer, TruckSerializer,
                        BoatSerializer, UserSerializer)

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class TruckList(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class TruckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class BoatList(generics.ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
