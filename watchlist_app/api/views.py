from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# app import
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import (WatchListSerializer, StreamPlatformSerializer, 
                                           ReviewSerializer)

from watchlist_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly


class ReviewCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)
    
    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        movie = WatchList.objects.get(pk=pk)
        
        user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=user)
        
        if review_queryset.exists():
            raise ValidationError("You have alerady reviewed this content!!")
        
        serializer.save(watchlist = movie, review_user=user)
        

class ReviewList(generics.ListAPIView): # get(), post()
    # queryset =  Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated] # Object level permission
    
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView): # get(), put(), delete()
    queryset =  Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly] # Object level permission
    



# class ReviewDetail(mixins.RetrieveModelMixin, # get req
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewtList(mixins.ListModelMixin, # get req
#                   mixins.CreateModelMixin, # post req
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


#================================
class WatchListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListDetailAV(APIView):

    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#=============================================



class StreamPlatformAV(APIView):

    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class StreamPlatformDetailAV(APIView):

    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## Genetic APIView













#===============================================================
    # @api_view(["GET", "POST"])
    # def movie_list(request):
    #     if request.method == "GET":
    #         movies = Movie.objects.all()
    #         serializer = MovieSerializer(movies, many=True)
    #         return Response(serializer.data)

    #     if request.method == "POST": # Create
    #         serializer = MovieSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors)

    # @api_view(["GET", "PUT", "DELETE"])
    # def movie_details(request, pk):

    #     if request.method == "GET":
    #         try:
    #             movie = Movie.objects.get(pk=pk)
    #         except Movie.DoesNotExist:
    #             return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
    #         serializer = MovieSerializer(movie)
    #         return Response(serializer.data)

    #     if request.method == "PUT": # Update
    #         movie = Movie.objects.get(pk=pk)
    #         serializer = MovieSerializer(movie, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     if request.method == "DELETE":
    #         movie = Movie.objects.get(pk=pk)
    #         movie.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
