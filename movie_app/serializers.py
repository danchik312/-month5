from rest_framework import serializers
from . import models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.movie
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.director
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.review
        fields = '__all__'