from django.shortcuts import render
from django.views import View

from .models import Movie


class MoviesView(View):
    #   Списък на филмите

    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        return render(request, 'movies/movies.html', {'movie_list': movies})


class MovieDetailView(View):
    #  Пълно описание на филмите

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})
