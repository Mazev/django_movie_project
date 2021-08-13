from django.shortcuts import render, redirect
from django.views import View

from .models import Movie
from django_movie_project.movies.forms import ReviewForm


class MoviesView(View):
    #   Списък на филмите

    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        return render(request, 'movies/movies_list.html', {'movie_list': movies})


class MovieDetailView(View):
    #  Пълно описание на филмите

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})


class AddReview(View):
    # Коментари към филма

    def post(self, request, pk, ):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()

        return redirect(movie.absolute_url())
