from django import forms

from .models import Song

class UploadSongForm(forms.ModelForm):
    album = forms.CharField(max_length=256, required=False)

    class Meta:
        model = Song
        fields = ['title','artist','audio_file',]