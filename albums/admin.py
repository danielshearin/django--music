from django.contrib import admin
from .models import Album
from .models import Artist

class AlbumInline(admin.TabularInline):
    model = Album

admin.site.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline, ]

admin.site.register(Album)
# admin.site.register(Artist)
