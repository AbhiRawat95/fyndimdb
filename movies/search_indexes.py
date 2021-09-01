import datetime
from haystack import indexes
from movies.models import Movie


class MovieIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    director = indexes.CharField(model_attr='director')
    genre = indexes.CharField(model_attr='genre')
    imdb_score = indexes.DecimalField(model_attr='imdb_score')
    popularity = indexes.DecimalField(model_attr='popularity')

    def get_model(self):
        return Movie

    def index_queryset(self, using=None):
        return self.get_model().objects.all()