from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Song, Album
from .forms import UploadSongForm

class SongListView(ListView):
    model = Song
    template_name = 'songs/home.html'
    ordering = ['title']

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
            print("---id---",id)
            print("--request.POST---",request.POST)
            print("--request.FILES---",request.FILES)
            form = UploadSongForm(request.POST, request.FILES)
        else:
            song = Song.objects.get(pk=id)
            form = UploadSongForm(request.POST, instance=song)

        print('---form is valid---', form.is_valid())
        if form.is_valid():
            instance = form.save(commit=False)
            album = form.cleaned_data.get('album')
            print("this is the instance.album ",instance.album)
            if album != '':
                music_album = Album.objects.get_or_create(name=album)
                instance.album=music_album[0]
                instance.save()
            else:
                instance.save()
        return redirect('songs:home')