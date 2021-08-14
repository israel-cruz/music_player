from django.urls import path

from .views import SongListView, upload_song_form

app_name = 'songs'

urlpatterns = [
    path('', SongListView.as_view(), name='home'),
    path('upload/', upload_song_form, name='upload'),
    path('upload/<int:id>/', upload_song_form, name='update'),
]