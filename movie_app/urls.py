from django.urls import path
from movie_app import views
urlpatterns = [
    path('api/v1/directors/', views.DirectorListView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailView.as_view()),
    path('api/v1/movies/', views.MovieListView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailView.as_view()),
    path('api/v1/reviews/', views.ReviewListView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailView.as_view()),
    path('api/v1/movies/reviews_stars/', views.MoviesReviewsView.as_view()),
    path('api/v1/director_movies/', views.DirectorMoviesCountView.as_view()),
]
