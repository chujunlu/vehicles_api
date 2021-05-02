from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from vehicles.views import CarList


class AnonymousTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
    
    def test_anonymous_usage(self):
        """Ensure routes are protected against anonymous usage.
        """
        request = self.factory.get('/cars')
        request.user = AnonymousUser()
        response = CarList.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
