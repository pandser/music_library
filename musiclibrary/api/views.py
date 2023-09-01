from rest_framework.viewsets import ModelViewSet

from api.models import Artist, Album, Song
from api.serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
