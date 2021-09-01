from haystack.backends import SQ
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from haystack.generic_views import SearchView
from movies.serializers import *


class MovieDataInsertion(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['post'],detail=False)
    def insert_movie_data(self, request):
        try:
            names = request.data['name']
            for x in names:
                final_genre = ','.join([str(elem) for elem in x['genre']])
                Movie.objects.create(title=x['name'], director=x['director'], popularity=x['99popularity'],
                                     imdb_score=x['imdb_score'],genre=final_genre)
            return Response({'message': 'All Entries Created.', 'status':status.HTTP_201_CREATED})
        except Exception as ex:
            return Response({'message': 'All Entries Failed.', 'status': status.HTTP_400_BAD_REQUEST})


class MoviesListingPage(ListAPIView):
    permission_classes = ()
    serializer_class = MovieSearchSerializer
    queryset = SearchQuerySet().all()

    def list(self,request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        data = {
            "data": serializer.data,
            }
        return self.get_paginated_response(data)


class AdminMoviesCreateAPI(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAddSearchSerializer


class AdminMoviesUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAddSearchSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        # movie_id = request.data.get('id')
        response = super().delete(request,*args,**kwargs)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response


class SearchMovie(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MovieSearchSerializer
    queryset_q = EmptySearchQuerySet()

    def get_queryset(self, *args, **kwargs):
        request = self.request
        queryset = SearchQuerySet().all()
        # Search Text
        if request.GET.get('q') is not None:
            query = request.GET.get('q').lower()
            queryset = queryset.filter(SQ(title=query)
                                       | SQ(director=query)
                                       | SQ(genre=query)
                                       )
        return queryset
