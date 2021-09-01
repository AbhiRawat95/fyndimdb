from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=False)
    director = models.TextField(null=True)
    genre = models.CharField(max_length=500, null=True)
    year = models.CharField(null=True, max_length=255)
    imdb_score = models.DecimalField(max_digits=4, decimal_places=2)
    popularity = models.DecimalField(max_digits=4, decimal_places=2)
    released = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    imdb_no_votes = models.CharField(max_length=255, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Cast(models.Model):
    movie = models.ForeignKey(Movie,null=False,on_delete=models.DO_NOTHING)
    cast_members = models.TextField(null=False)

    def __str__(self):
        return self.movie.title



