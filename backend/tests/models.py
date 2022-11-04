from django.db import models
from django.contrib.auth.models import User
import uuid

class Test(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=128, null=False)
    description = models.CharField(max_length=255, blank=True)
    who_create = models.ForeignKey(User, on_delete=models.CASCADE)
    



