from dataclasses import fields
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

# ============== serializers.ModelSerializer ==========================

class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ["id", "name", "description"] # hiding "active" field
        # exclude = ["active"] # hiding "active" field
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) # must be "watchlist" to form relation
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
    







# ============== serializers.Serializer ==========================

# def name_length(value): # Validators (3rd type)
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")


# class MovieSerializer(serializers.Serializer): # model name is "Movie", so serializer name is "MovieSerializer"
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, vaalidate_data): # POST
#         return Movie.objects.create(**vaalidate_data)
    
#     def update(self, instance, validated_data): # PUT # instance = old values, validated_data = updated values
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
        
#         instance.save()
#         return instance
    
#     def validate(self, data): # object level validator
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title and Description can not be same!!")
    
#     # def validate_name(self, value): # Field-level validation
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     else:
#     #         return value