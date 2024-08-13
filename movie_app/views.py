from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from django.forms import model_to_dict
from rest_framework import status
from . import serializers

@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    directors = models.director.objects.all()
    list_= serializers.DirectorSerializer(directors, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def director_detail_api_view(request, id):
    try:
        director = models.director.objects.get(id=id)
    except models.director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found!'})
    data = serializers.DirectorSerializer(director).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movies = models.movie.objects.all()
    list_= serializers.MovieSerializer(movies, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def movie_detail_api_view(request, id):
    try:
        movies = models.movie.objects.get(id=id)
    except models.movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found!'})
    data = serializers.MovieSerializer(movies).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = models.review.objects.all()
    list_= serializers.ReviewSerializer(reviews, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def review_detail_api_view(request, id):
    try:
        reviews = models.review.objects.get(id=id)
    except models.review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found!'})
    data = serializers.ReviewSerializer(reviews).data
    return Response(data=data)