from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def home(request):
    movie_count = Movie.objects.count()
    recent_movies = Movie.objects.order_by('-id')[:5]
    return render(request, 'catalog/index.html', {
        'movie_count': movie_count,
        'recent_movies': recent_movies,
    })

def movie_list(request):
    movies = Movie.objects.all().order_by('-release_date')
    return render(request, 'catalog/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'catalog/movie_detail.html', {'movie': movie})

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            from django.contrib.auth.models import User
            movie.added_by = User.objects.first() or User.objects.create_user(username='default', password='123456')
            movie.save()
            form.save_m2m()
            messages.success(request, f'《{movie.title}》add successfully！')
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'catalog/movie_add.html', {'form': form})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        title = movie.title
        movie.delete()
        messages.success(request, f'《{title}》deleted.')
        return redirect('movie_list')
    return render(request, 'catalog/movie_confirm_delete.html', {'movie': movie})