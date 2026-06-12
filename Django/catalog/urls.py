from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/add/', views.movie_add, name='movie_add'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
]
