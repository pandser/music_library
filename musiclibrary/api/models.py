from django.db import models


class Artist(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Исполнитель'
    )

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='album',
        verbose_name='Исполнитель',
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска',
    )

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return f'{self.artist} {self.year}' 

class Song(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название песни',
    )

    class Meta:
        verbose_name = 'Название песни'
        verbose_name_plural = 'Название песни'
        
    def __str__(self):
        return self.name


class SongInAlbum(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='songs',
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='album',
    )
    number = models.IntegerField(
        verbose_name='Номер трека',
    )

    class Meta:
        ordering = ('number',)
