from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from django.forms import model_to_dict
from rest_framework import status
@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    directors = models.director.objects.all()
    list=[]
    for i in directors:
        list.append(model_to_dict(i))
    return Response(data={}, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movies = models.movie.objects.all()
    list=[]
    for t in movies:
        list.append(model_to_dict(t))
    return Response(data={}, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = models.review.objects.all()
    list=[]
    for e in reviews:
        list.append(model_to_dict(e))
    return Response(data={}, status=status.HTTP_200_OK)