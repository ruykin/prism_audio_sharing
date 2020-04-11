from django import forms
from .models import UploadedAudio, SharedFiles


class UploadedAudioForm(forms.ModelForm):
    class Meta:
        model = UploadedAudio
        fields = ('document',)
