from django.contrib import admin
from .models import UserProfile, Genre, Movie

admin.site.register(UserProfile)
admin.site.register(Genre)
admin.site.register(Movie)