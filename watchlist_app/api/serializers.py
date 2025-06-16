from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short!")


class MovieSerilizer(serializers.Serializer): # model name is "Movie", so serializer name is "MovieSerilizer"
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
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
    
    def validate(self, data): # object level validator
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Title and Description can not be same!!")
    
    # def validate_name(self, value): # Field-level validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value