import json
from django.contrib.auth.models import AnonymousUser
from django.http import response
from django.test import TestCase
from django.test.client import RequestFactory
from users.models import CustomUser
from django.test import Client
# Create your tests here.

class UserTest(TestCase):
    def test_user_creation_default(self):
        user = CustomUser.objects.create_user('username1', 'jab@gmail.com', 'password1')
        # checking the input is assigned to the correct field
        self.assertEqual(user.username, 'username1')
        self.assertEqual(user.email, 'jab@gmail.com')
        self.assertTrue(user.check_password('password1'))
        # checking user model's Primary Key is UID
        self.assertEqual(user.pk, user.id) # >> True, user.pk => user.id => 1

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from rest_framework.test import RequestsClient
from users import views
class ApiIntegrationTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.UserLogin.as_view()
        self.uri = '/login/'
        self.client = APIClient()
    
class UserLoginFactoryTest(APITestCase):
    """unittest: test user login API with DRF factory toolkit"""
    def setUp(self):
        """
        steps:
            -> must setup separated database model
            -> must use 'create_user' rather than 'create' in models
            -> testing basic login api function, check JWT token received
        """
        self.factory = APIRequestFactory()
        self.url = 'api/users/login/'
        self.view = views.UserLogin.as_view()
        self.credentials = {
            'username': 'username1',
            'password': 'password1'}
        self.user = CustomUser.objects.create_user(**self.credentials) # avoid using User.objects.create(...), will fail
        # CustomUser.objects.create(username='username1', password='password1') # WRONG!!!

    def test_login_user(self):
        request = self.factory.post(self.url, json.dumps(self.credentials), content_type='application/json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        
    def test_login_jwt_token_retrieve(self):
        request = self.factory.post(self.url, json.dumps(self.credentials), content_type='application/json')
        response = self.view(request)
        self.assertTrue('token' in response.data)

    def test_login_required_api(self):
        request = self.factory.post(self.url, json.dumps(self.credentials), content_type='application/json')
        response = self.view(request)
        
        id = response.data['id']
        token = response.data['token']
        jwt_header = {'Authorization': f'JWT {token}'}
        c = RequestsClient()
        response = c.get(f'http://testserver/api/users/{id}/posts/', headers=jwt_header)
        self.assertEqual(response.status_code, 200)
        