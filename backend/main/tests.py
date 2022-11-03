from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from . import models


class Tests(LiveServerTestCase):
    
    def test_cant_create_test_without_auth(self):
        res = self.client.post("/new", {"name": "lalalal", "description": "adedae"})
        self.assertEqual(res.status_code, 401)


