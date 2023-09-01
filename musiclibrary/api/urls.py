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

# router.register(
#     r'album',
#     AlbumViewSet,
#     basename='album',
# )


urlpatterns = [
    path('', include(router.urls)),
]