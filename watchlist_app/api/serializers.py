from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerilizer(serializers.Serializer): # model name is "Movie", so serializer name is "MovieSeilizers"
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, vaalidate_data): # POST
        return Movie.objects.create(**vaalidate_data)
    
    def update(self, instance, validated_data): # PUT # instance = old values, validated_data = updated values
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)    
        
        instance.save()
        return instance
    