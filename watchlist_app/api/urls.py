from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformDetailAV, StreamPlatformAV
urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchListDetailAV.as_view(), name="movie_details"),
    path("stream/", StreamPlatformAV.as_view(), name="platform_stream-list"),
    path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream_platform_details"),
]