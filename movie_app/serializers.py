from rest_framework import serializers
from .models import director, movie, review
from datetime import date, timedelta
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = director
        fields = '__all__'

    def validate_birth_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Дата рождения не может быть в будущем.")
        return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = '__all__'

    def validate_duration(self, value):
        if value < timedelta(minutes=1):
            raise serializers.ValidationError("Продолжительность фильма должна быть не менее 1 минуты.")
        if value > timedelta(hours=4):
            raise serializers.ValidationError("Продолжительность фильма не должна превышать 4 часа.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Имя должно содержать не менее 3 символов.")
        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError("Имя должно содержать только буквы.")
        return value
