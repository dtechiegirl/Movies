from django.db import models

# Create your models here.
# class Movie(models.Model):
#     name = models.CharField(max_length=20),
#     rating = models.FloatField(max_length=3),
#     releaseDate= models.IntegerField(max_length=30),
#     genre = models.CharField(max_length= 20),
#     image = models.CharField(max_length=3),

class Movie(models.Model):
    name = models.CharField(max_length=300, default = "John DOE")
    rating = models.FloatField(max_length=2, default= 1.0)
    genre = models.CharField(max_length=300, default= "African")
    image = models.CharField(max_length=300, default = " ")
    released = models.DateTimeField(auto_now = True)
    def __str__(self):
        return (self.name)

class Registration(models.Model):
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
