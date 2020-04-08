from os import path
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return path.join('documents/', filename)


class UploadedAudio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to=content_file_name)
    uploaded_at = models.DateTimeField(auto_now_add=True)
