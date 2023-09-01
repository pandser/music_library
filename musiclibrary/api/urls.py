from django.urls import path, include
from rest_framework import routers

from api.views import ArtistViewSet, AlbumViewSet


app_name = 'api'
router = routers.DefaultRouter()

router.register(
    r'artist',
    ArtistViewSet,
    basename='artist',
)

urlpatterns = [
    path('', include(router.urls)),
]