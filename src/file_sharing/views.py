import mimetypes
from os import path, access, R_OK, stat
from wsgiref.util import FileWrapper

from django.core import serializers
from django.contrib.auth.models import User
import json
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.encoding import smart_str
from scipy.io.wavfile import read, write
from numpy import array

from .forms import UploadedAudioForm, UploadedAudio, SharedFiles


def friends(request, *args, **kwargs):
    users = User.objects.filter(~Q(id=request.user.id))
    data = serializers.serialize('json', list(users), fields=('id', 'username',))
    return render(request, 'file_sharing/friends.html', {
        'data': json.loads(data),
        'audio': kwargs['audio_id']
    })


def share(request, *args, **kwargs):
    share_by = request.user
    uploaded_audio = UploadedAudio.objects.get(id=kwargs['audio_id'])
    share_to = User.objects.get(id=kwargs['user_id'])
    SharedFiles.objects.create(shared_by=share_by, shared_to=share_to, uploaded_audio=uploaded_audio)
    return redirect('home')


def download(request, *args, **kwargs):
    uploaded_audio = UploadedAudio.objects.get(id=kwargs['audio_id'])
    file_path = 'media/{}'.format(str(uploaded_audio.document))
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="audio/wave")
        response['Content-Disposition'] = 'inline; filename=' + path.basename(file_path)
        return response


def upload(request):
    if request.method == 'POST':
        form = UploadedAudioForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            saved_object = UploadedAudio.objects.get(id=obj.id)
            file_path = saved_object.document
            head, tail = path.split(str(file_path))
            sample_rate, data = read(file_path)
            d = []
            for i in data:
                d.append([i[0], i[1]])
            d = array(d)
            for i in d:
                # to encrypt
                i[0], i[1] = i[1], i[0] + 2000000000
                # to de-encrypt
                # i[1], i[0] = i[0], i[1] - 2000000000
            write('media/documents/' + tail, sample_rate, d)
            return redirect('home')
    else:
        form = UploadedAudioForm()
    return render(request, 'file_sharing/upload.html', {
        'form': form
    })
