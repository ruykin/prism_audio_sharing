from django.urls import path

from . import views

urlpatterns = [
    path('', views.friends, name='friends'),
    path('upload/', views.upload, name='upload'),
    path('friends/<int:audio_id>/', views.friends, name='friends'),
    path('share/<int:audio_id>/<int:user_id>', views.share, name='share'),
]