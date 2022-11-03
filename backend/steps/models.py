from django.db import models
import uuid
from tests.models import Test

class Step(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
