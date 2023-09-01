from rest_framework import serializers

from api.models import Album, Artist, Song, SongInAlbum


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'name',
        )


class SongInAlbumSerializer(serializers.ModelSerializer):
    song = SongSerializer()
    class Meta:
        model = SongInAlbum
        fields = (
            'number',
            'song',
        )


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(read_only=True)
    songs = SongInAlbumSerializer(many=True)
    class Meta:
        model = Album
        fields  = (
            'artist',
            'year',
            'songs',
        )


class ArtistSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True)
    class Meta:
        model = Artist
        fields = (
            'name',
            'album',
        )

    def create(self, validated_data):
        if 'album' not in self.initial_data:
            artist, status = Artist.objects.create(**validated_data)
            return artist
        albums = validated_data.pop('album')
        artist, status = Artist.objects.create(**validated_data)
        for album in albums:
            songs = album.pop('songs')
            album, status = Album.objects.get_or_create(
                artist=artist,
                year=album.get('year')
            )
        for song in songs:
            track, status = Song.objects.get_or_create(**song.pop('song'))
            SongInAlbum.objects.create(song=track, album=album, **song)
        return artist
    
    def update(self, instance, validated_data):
        albums = validated_data.pop('album')
        for key, value in validated_data.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        
        if albums:
            for album in albums:
                songs = album.pop('songs')
                album, status = Album.objects.get_or_create(
                    artist=instance,
                    year=album.get('year')
                )
            for song in songs:
                track, status = Song.objects.get_or_create(**song.pop('song'))
                SongInAlbum.objects.get_or_create(
                    song=track,
                    album=album, **song
                )
        instance.save()
        return instance
