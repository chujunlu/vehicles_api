from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Car, Truck, Boat
from .serializers import (CarSerializer, TruckSerializer,
                        BoatSerializer, UserSerializer)


@api_view(['GET'])
def api_root(request):
    return Response({
        'cars': reverse('car-list', request=request),
        'trucks': reverse('truck-list', request=request),
        'boats': reverse('boat-list', request=request),
        'users': reverse('user-list', request=request)
    })

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
