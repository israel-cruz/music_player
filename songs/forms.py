from django import forms

from .models import Song

class UploadSongForm(forms.ModelForm):
    album = forms.CharField(max_length=256, required=False, label='Album (Optional)')

    class Meta:
        model = Song
        fields = ['title','artist','audio_file','image']
        labels = {
            'artist':'Artist (Optional)',
            'audio_file':'Song file',
        }

class DownloadYoutubeForm(forms.Form):
    url = forms.CharField(max_length=256, required=False, label='Paste your youtube link here')