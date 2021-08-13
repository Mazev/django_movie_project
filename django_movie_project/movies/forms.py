from django import forms

from django_movie_project.movies.models import Reviews

class ReviewForm(forms.ModelForm):
    # форма за коментарите

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')