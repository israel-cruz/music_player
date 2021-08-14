from django.contrib import admin

from .models import Album, Song

admin.site.register(Song)
admin.site.register(Album)
