from django.urls import path

from .views import SongListView, upload_song_form, download_youtube_form, json_songs

app_name = 'songs'

urlpatterns = [
    path('', SongListView.as_view(), name='home'),
    path('upload/', upload_song_form, name='upload'),
    path('song/<int:id>/', upload_song_form, name='update'),
    path('download/', download_youtube_form, name='download'),
    path('json_songs/', json_songs, name='json-songs'),
]