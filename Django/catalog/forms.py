from django import forms
from .models import Movie
from datetime import date

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'duration', 'rating',
                 'is_favorite', 'difficulty', 'summary', 'genres', 'poster']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'genres': forms.CheckboxSelectMultiple(),
            'summary': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'title': 'film name',
            'release_date': 'data',
            'duration': 'duration（mins）',
            'rating': 'marks（0-10）',
            'is_favorite': 'set favorite',
            'difficulty': 'difficulty',
            'summary': 'introduce',
            'genres': 'film genre',
            'poster': 'poster',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError('at least 2 characters')
        return title

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date and release_date > date.today():
            raise forms.ValidationError('data cant be future')
        return release_date