from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import UploadedAudioForm


def friends(request):
    users = User.objects.filter(~Q(username='admin'))
    data = serializers.serialize('json', list(users), fields=('username',))
    return data


def upload(request):
    if request.method == 'POST':
        form = UploadedAudioForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    else:
        form = UploadedAudioForm()
    return render(request, 'file_sharing/upload.html', {
        'form': form
    })
