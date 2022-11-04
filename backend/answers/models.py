from django.db import models
import uuid
from steps.models import Step

class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=128, null=False)
    is_true = models.BooleanField()
    step = models.ForeignKey(Step, related_name='answers' ,on_delete=models.CASCADE)


