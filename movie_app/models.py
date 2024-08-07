from django.db import models



class director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    duration=models.DurationField()
    director = models.ForeignKey(director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class review(models.Model):
    text = models.CharField(max_length=150)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text