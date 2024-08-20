from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from rest_framework import status
from . import serializers



@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = models.director.objects.all()
        serializer = serializers.DirectorSerializer(directors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = models.director.objects.get(id=id)
    except models.director.DoesNotExist:
        return Response({'error': 'Режиссер не найден'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.DirectorSerializer(director)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = models.movie.objects.all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = models.movie.objects.get(id=id)
    except models.movie.DoesNotExist:
        return Response({'error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = models.review.objects.all()
        serializer = serializers.ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = models.review.objects.get(id=id)
    except models.review.DoesNotExist:
        return Response({'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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