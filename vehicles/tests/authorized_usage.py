from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import (APIRequestFactory, APITestCase,
        force_authenticate)

from vehicles.models import Car
from vehicles.views import CarList, CarDetail


SAMPLE_CAR = {
    'make': 'Lexus',
    'model': 'RX 350',
    'year': '2019',
    'seats': 5,
    'color': 'Eminent White Pearl',
    'vin': '2T2BZMCA7KC201540',
    'current_mileage': 17004,
    'service_interval': 'every 12 months',
    'next_service': '2022-06-01'
}

class AuthorizedTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='olivia', email='olivia@gmail.com', password='for_test_purpose'
        )
        self.factory = APIRequestFactory()

        # Create a car object in database to be retrieved in test cases
        url = reverse('car-list')
        request = self.factory.post(url, SAMPLE_CAR, format='json')
        force_authenticate(request, user=self.user)
        CarList.as_view()(request)

    def test_get_car_list(self):
        """
        Ensure we can list all cars.
        """
        url = reverse('car-list')
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = CarList.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_car_detail(self):
        """
        Ensure we can read a single car object.
        """
        request = self.factory.get('cars/1')
        force_authenticate(request, user=self.user)
        response = CarDetail.as_view()(request, pk='1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vin'], SAMPLE_CAR['vin'])

    def test_post_car(self):
        """
        Ensure we can create a new car object.
        """
        url = reverse('car-list')
        data = {
            'make': 'Jaguar',
            'model': 'F-PACE 25t Premium',
            'year': '2018',
            'seats': 5,
            'color': 'Narvik Black',
            'vin': 'SADCJ2FX5JA268410',
            'current_mileage': 15336,
            'service_interval': 'every 15 months',
            'next_service': '2023-5-6'
        }
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = CarList.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 2)

    def test_update_car(self):
        """
        Ensure we can update part of a car object.
        """
        new_next_service = '2022-10-01'
        request = self.factory.patch('cars/1', {'next_service': new_next_service})
        force_authenticate(request, user=self.user)
        response = CarDetail.as_view()(request, pk='1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['next_service'], new_next_service)

    def test_delete_car(self):
        """
        Ensure we can delete a car object.
        """
        request = self.factory.delete('cars/1')
        force_authenticate(request, user=self.user)
        response = CarDetail.as_view()(request, pk='1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
