from os import path, access, R_OK
from django.core import serializers
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from scipy.io.wavfile import read, write
from numpy import array

from .forms import UploadedAudioForm, UploadedAudio


def friends(request):
    users = User.objects.filter(~Q(username='admin'))
    data = serializers.serialize('json', list(users), fields=('username',))
    return data


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
            write('media/documents/'+tail, sample_rate, d)
            return redirect('home')
    else:
        form = UploadedAudioForm()
    return render(request, 'file_sharing/upload.html', {
        'form': form
    })
