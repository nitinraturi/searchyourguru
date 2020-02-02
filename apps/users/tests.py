from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from . import services as user_services
from . import constants as user_constants

class RegisterTest(APITestCase):
    def setup(self):
        self.test_user = user_services.create_user('testuser@gmail.com','test@123',name="Test User",user_type=user_constants.STUDENT)
        self.create_url = reverse('auth:register')

    def test_create_user(self):
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }

        response = self.client.post(self.create_url , data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
