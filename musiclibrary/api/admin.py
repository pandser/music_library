from django.contrib import admin

from api.models import Album, Artist, Song, SongInAlbum


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'artist',
        'year',
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(SongInAlbum)
class SongInAlbumAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'album',
        'song',
        'number',
    )
