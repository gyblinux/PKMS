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