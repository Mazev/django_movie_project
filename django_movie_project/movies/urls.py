from django.urls import path

from django_movie_project.movies import views

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('<int:pk>/', views.MovieDetailView.as_view()),
]