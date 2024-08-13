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

@api_view(http_method_names=['GET'])
def movies_reviews_api_view(request):
    movies = models.movie.objects.all()
    data = []
    for movie in movies:
        movie_data = serializers.MovieSerializer(movie).data
        reviews = models.review.objects.filter(movie=movie)
        movie_data['reviews'] = serializers.ReviewSerializer(reviews, many=True).data
        total_stars = sum(review.stars for review in reviews)
        count_reviews = reviews.count()
        avg_rating = total_stars / count_reviews if count_reviews > 0 else 0
        movie_data['average_rating'] = round(avg_rating, 2)
        data.append(movie_data)
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def directors_with_movie_count_api_view(request):
    directors = models.director.objects.all()
    data = []
    for director in directors:
        director_data = serializers.DirectorSerializer(director).data
        movies_count = models.movie.objects.filter(director=director).count()
        director_data['movies_count'] = movies_count
        data.append(director_data)
    return Response(data=data, status=status.HTTP_200_OK)