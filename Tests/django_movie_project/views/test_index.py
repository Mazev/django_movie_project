from django.test import TestCase
from django.urls import reverse, resolve

from django_movie_project import movies
from django_movie_project.movies.views import MoviesView


class TestUrls(TestCase):
    def test_list_url_is_resolvet(self):
        url = reverse('movies/movies_list.html')
        print(resolve(url))
        self.assertEqual(resolve(url).func, MoviesView)

