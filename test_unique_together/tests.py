from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient

# Create your tests here.
class TweetTest(TestCase):
    @staticmethod
    def _create_user(username, email, password, is_admin, is_staff):
        if is_admin:
            return User.objects.create_superuser(username, email, password)
        if is_staff:
            return User.objects.create_user(username, email, password, is_staff=is_staff)
        else:
            # not admin nor staff -> normal user
            return User.objects.create_user(username, email, password)

    def create_user(self, username=None, email=None, password=None, is_admin=False, is_staff=False):
        if username is None:
            username = "TEST_USERNAME"
        if password is None:
            password = "TEST_PASSWORD"
        if email is None:
            email = "TEST_EMAIL@gmail.com"

        return self._create_user(username, email, password, is_admin, is_staff)

    @property
    def anonymous_client(self):
        self._anonymous_client = APIClient()
        return self._anonymous_client

    def create_and_authenticate_client(self,
                                       username=None,
                                       email=None,
                                       password=None,
                                       is_admin=False,
                                       is_staff=False):

        user = self.create_user(username, email, password, is_admin, is_staff)
        client = APIClient()
        client.force_authenticate(user)
        return [user, client]

    def setUp(self):
        self.registered_user, self.registered_client = self.create_and_authenticate_client(
            is_admin=False,
            is_staff=False
        )

    def test_create(self):
        data = {
            'content': "abcd",
            'dummy_column': "abcd",
        }
        
        url = '/api/tweets/'
        
        response = self.registered_client.post(url, data)
        print(response.data)
        self.assertEqual(response.status_code, 201)
        