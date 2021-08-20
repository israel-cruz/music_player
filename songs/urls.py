from django.urls import path

from .views import SongListView, ManageListView, upload_song_form, download_youtube_form, delete_song_view, json_songs

app_name = 'songs'

urlpatterns = [
    path('', SongListView.as_view(), name='home'),
    path('manage/', ManageListView.as_view(), name='manage'),
    path('upload/', upload_song_form, name='upload'),
    path('<int:id>/', upload_song_form, name='update'),
    path('download/', download_youtube_form, name='download'),
    path('delete/<int:id>/', delete_song_view, name='delete'),
    path('json_songs/', json_songs, name='json-songs'),
]