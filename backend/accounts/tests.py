from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Tests(LiveServerTestCase):
    
    def test_token_creates_after_user_registration(self):
        user = User.objects.create(username="lalal", password="123")
        Token.objects.get(user=user)
