from django.db import models
import uuid
from tests.models import Test

class Step(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=True)
    condition = models.JSONField(null=False, verbose_name="условие задания в 'pretty' формате") # rendering at frontend
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='steps')
