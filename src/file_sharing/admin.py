from django.contrib import admin

from .models import UploadedAudio, SharedFiles

admin.site.register(UploadedAudio)
admin.site.register(SharedFiles)
