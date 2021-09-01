from rest_framework import serializers

from movies.models import Movie


class MovieSearchSerializer(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.SerializerMethodField()
    director = serializers.CharField()
    genre = serializers.SerializerMethodField()
    imdb_score = serializers.DecimalField(max_digits=4,decimal_places=2)
    popularity = serializers.DecimalField(max_digits=4,decimal_places=2)

    def get_id(self,obj):
        return obj.pk

    def get_genre(self,obj):
        return obj.genre


class MovieAddSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields ='__all__'