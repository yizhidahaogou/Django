from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, verbose_name='introduce')
    birth_date = models.DateField(null=True, blank=True, verbose_name='birthday')
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='film genre')
    description = models.TextField(blank=True, verbose_name='dercribe')

    def __str__(self):
        return self.name

class Movie(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', '简单'),
        ('medium','中等'),
        ('hard','困难'),
    ]
    title = models.CharField(max_length=200, verbose_name='film name')
    release_date = models.DateField(verbose_name='data')
    duration = models.IntegerField(verbose_name='duration（mins）',
                                   validators=[MinValueValidator(1), MaxValueValidator(999)])
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='marks',
                                validators=[MinValueValidator(0), MaxValueValidator(10)])
    is_favorite = models.BooleanField(default=False, verbose_name='likes?')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES,
                                  default='medium', verbose_name='difficulty')
    summary = models.TextField(blank=True, verbose_name='introduce')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies',
                                 verbose_name='adder')
    genres = models.ManyToManyField(Genre, related_name='movies', verbose_name='film genre')
    poster = models.ImageField(upload_to='posters/', blank=True, verbose_name='poster')

    def __str__(self):
        return self.title