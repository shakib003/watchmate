from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (ReviewDetail, ReviewtList, 
                                     WatchListAV, WatchListDetailAV, 
                                     StreamPlatformDetailAV, StreamPlatformAV)
from watchlist_app.models import Review

# watch/...
urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchListDetailAV.as_view(), name="movie_details"),
    path("stream/", StreamPlatformAV.as_view(), name="platform_stream-list"),
    path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream_platform_details"),
    
    path("review", ReviewtList.as_view(), name="review-list"),
    path("review/<int:pk>", ReviewDetail.as_view(), name="review-detail"),
]