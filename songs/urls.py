from django.urls import path

from .views import SongListView, upload_song_form, download_youtube_form

app_name = 'songs'

urlpatterns = [
    path('', SongListView.as_view(), name='home'),
    path('upload/', upload_song_form, name='upload'),
    path('song/<int:id>/', upload_song_form, name='update'),
    path('download/', download_youtube_form, name='download'),
]