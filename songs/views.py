from django.shortcuts import render, redirect
from django.views.generic import ListView

import pafy
import os

from .models import Song, Album
from .forms import UploadSongForm, DownloadYoutubeForm

class SongListView(ListView):
    model = Song
    template_name = 'songs/home.html'
    ordering = ['title']
    context_object_name = 'songs'

def download_youtube_form(request):
    form = DownloadYoutubeForm()

    if request.method == 'POST':
        form = DownloadYoutubeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            audio = pafy.new(url)
            best = audio.getbestaudio(preftype="m4a")
            path = str(os.getcwd()) + '/media/songs/'
            best.download(filepath=path)
            file = str('songs/' + audio.title + '.m4a')
            song = Song.objects.get_or_create(title=audio.title, artist=audio.author, time_length=audio.length, audio_file=file)
        return redirect('songs:home')
    
    context = {
        'form':form,
    }

    return render(request, 'songs/download_song.html', context)

def upload_song_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = UploadSongForm()
        else:
            song = Song.objects.get(pk=id)
            form = UploadSongForm(instance=song)
        context = {'form':form}
        return render(request, 'songs/upload_song.html', context)

    if request.method == 'POST':
        if id == 0:
            form = UploadSongForm(request.POST, request.FILES)
        else:
            song = Song.objects.get(pk=id)
            form = UploadSongForm(request.POST, instance=song)

        if form.is_valid():
            instance = form.save(commit=False)
            album = form.cleaned_data.get('album')
            if album != '':
                music_album = Album.objects.get_or_create(name=album)
                instance.album=music_album[0]
                instance.save()
            else:
                instance.save()
        return redirect('songs:home')