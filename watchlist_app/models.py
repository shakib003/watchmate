from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    titile = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titile























# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.name