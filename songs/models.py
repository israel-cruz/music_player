from django.db import models

from PIL import Image

from .audio_tools import validate_is_audio, get_audio_length

class Album(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=256)
    artist = models.CharField(max_length=256, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    time_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    image = models.ImageField(default='img/default.jpg', upload_to='img/', blank=True, null=True)
    image_url = models.CharField(max_length=256, default='media/img/default.jpg', blank=True, null=True)
    audio_file = models.FileField(upload_to='songs', validators=[validate_is_audio], null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.time_length:
            audio_length = get_audio_length(self.audio_file)
            self.time_length = f'{audio_length:.2f}'
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title