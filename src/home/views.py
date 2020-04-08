from os import path

from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import TemplateView
from file_sharing.models import UploadedAudio
import json

from scipy.io.wavfile import read, write
from numpy import array, int16, max, abs, float_, sin, arcsin


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        users_uploaded_audio = UploadedAudio.objects.filter(user=self.request.user)
        users_uploaded_audio = json.loads(serializers.serialize('json', list(users_uploaded_audio)))
        context = locals()
        context['users_uploaded_audio'] = users_uploaded_audio
        return context


class PlayView(TemplateView):
    template_name = "play.html"

    def get_context_data(self, id, *args, **kwargs):
        audio = UploadedAudio.objects.get(id=id)
        context = locals()
        sample_rate, data = read(audio.document)
        d = []
        for i in data:
            d.append([i[0], i[1]])
        d = array(d)
        for i in d:
            i -= 100000000000
        head, tail = path.split(str(audio.document))
        write('media/temp/'+tail, sample_rate, d)
        context['audio_link'] = 'media/temp/'+tail
        return context
