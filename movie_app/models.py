from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class director(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    name = models.CharField(max_length=30, null=True)
    birth_date = models.DateField(default='2000-01-01')
    nationality = models.CharField(max_length=100, default='Unknown')
    email = models.EmailField(default="@gmail.com", null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Director"

class movie(models.Model):
    title=models.CharField(max_length=200 ,null=True )
    description=models.TextField(max_length=1000, null=True)
    duration=models.DurationField()
    director = models.ForeignKey(director, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True
    )
    photo = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Untitled Movie"

STAR_CHOICES = (
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
)
class review(models.Model):
    name = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=150 , null=False)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=STAR_CHOICES , default=1)
    email = models.EmailField(default="@gmail.com", null=True)


    def __str__(self):
        return self.name if self.name else "Anonymous Review"


