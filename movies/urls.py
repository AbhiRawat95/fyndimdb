from django.urls import path,include
from rest_framework import routers
from movies.views import *
from django.conf.urls import url

routers = routers.DefaultRouter()
routers.register(r'movie-create', MovieDataInsertion, basename='moviecreate')
urlpatterns = [
    path('', include(routers.urls)),
    url(r'^prodv1/movies-list/$', MoviesListingPage.as_view(), name='rest-movies-lists'),
    url(r'^prodv1/add-new-movie/$', AdminMoviesCreateAPI.as_view(), name='add-to-movie-lists'),
    path('prodv1/update-movie/<int:id>/', AdminMoviesUpdateDeleteAPI.as_view(), name='update-movie-lists'),
    path('prodv1/search/', SearchMovie.as_view(), name='update-movie-lists'),
]