from django import forms
from .models import UploadedAudio


class UploadedAudioForm(forms.ModelForm):
    class Meta:
        model = UploadedAudio
        fields = ('document',)
