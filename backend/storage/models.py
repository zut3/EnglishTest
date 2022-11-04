from django.db import models
import uuid
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='./', null=False)

    def save(self, *args, **kwargs):
        print(dir(self.image))
        self.image.file.filename = str(self.id)
        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Image)
def delete_file_from_disk(sender, instance=None, created=False, **kwargs):
    if instance:
        path = instance.image.path
        os.remove(path)
