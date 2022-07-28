from django.contrib import admin

# Register your models here.
from .models import Movie, Registration
admin.site.register(Movie)
admin.site.register(Registration)