from django.test import TestCase
from users.models import CustomUser
# Create your tests here.

class UserTest(TestCase):
    def test_user_creation_default(self):
        user = CustomUser.objects.create_user('username1', 'jab@gmail.com', 'password1');
        # checking the input is assigned to the correct field
        self.assertEqual(user.username, 'username1')
        self.assertEqual(user.email, 'jab@gmail.com')
        self.assertTrue(user.check_password('password1'))
        # checking user model's Primary Key is UID
        self.assertEqual(user.pk, user.id) # >> True, user.pk => user.id => 1

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from users import views
class ApiIntegrationTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.loginview = views.UserLogin.as_view()
        self.uri = '/login/'
        self.client = APIClient()
    def test_login(self):
        self.client.login(username="username1", password="password1")
        
    
    