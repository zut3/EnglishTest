from django.db import models
import uuid

class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    """Задания внутри теста"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=True, default='')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class Answer(models.Model):
    """Ответы на step'ы"""
    text = models.CharField(max_length=128, null=False)
    is_true = models.BooleanField()
    step = models.ForeignKey(Step, on_delete=models.CASCADE)


