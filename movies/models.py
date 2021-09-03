from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# Create your models here.


class Movie(models.Model):
    # Model to store the basic details of the movie
    title = models.CharField(max_length=255, unique=False)
    director = models.TextField(null=True)
    genre = models.CharField(max_length=500, null=True)
    year = models.CharField(null=True, max_length=255)
    imdb_score = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(10)])
    popularity = models.DecimalField(max_digits=4, decimal_places=2)
    released = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    imdb_no_votes = models.CharField(max_length=255, null=True)
    movie_poster = models.ImageField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Cast(models.Model):
    # Details of cast attached to a movie
    movie = models.ManyToManyField(Movie)
    name = models.TextField(null=False)
    age = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True)
    display_picture = models.ImageField(null=True)

    def __str__(self):
        return self.name


class MovieReview(models.Model):
    # Consist of reviews
    movie = models.ForeignKey(Movie, null=False, on_delete=models.DO_NOTHING)
    review = models.TextField(null=True)
    reviewed_by = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.movie.title

