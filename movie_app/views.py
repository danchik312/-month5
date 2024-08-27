from rest_framework import status, views, generics
from rest_framework.response import Response
from . import models, serializers

class DirectorListView(generics.ListCreateAPIView):
    queryset = models.director.objects.all()
    serializer_class = serializers.DirectorSerializer

class DirectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.director.objects.all()
    serializer_class = serializers.DirectorSerializer
    lookup_field = 'id'

class MovieListView(generics.ListCreateAPIView):
    queryset = models.movie.objects.all()
    serializer_class = serializers.MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'

class ReviewListView(generics.ListCreateAPIView):
    queryset = models.review.objects.all()
    serializer_class = serializers.ReviewSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'

class MoviesReviewsView(views.APIView):
    def get(self, request):
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

class DirectorMoviesCountView(views.APIView):
    def get(self, request):
        directors = models.director.objects.all()
        data = []
        for director in directors:
            director_data = serializers.DirectorSerializer(director).data
            movies_count = models.movie.objects.filter(director=director).count()
            director_data['movies_count'] = movies_count
            data.append(director_data)
        return Response(data=data, status=status.HTTP_200_OK)