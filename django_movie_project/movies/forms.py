from django import forms

from django_movie_project.movies.models import Reviews, RatingStar, Rating


class ReviewForm(forms.ModelForm):
    # форма за коментарите

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class RatingForm(forms.ModelForm):
    # Формата добавя рейтинг

    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)
