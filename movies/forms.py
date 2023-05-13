from django import forms

from .models import Movie, MultiMovieSet, movie_year_factory


class MovieCreateUpdateForm(forms.ModelForm):
    title = forms.CharField()
    year = forms.IntegerField()
    multi_movie_sets = forms.ModelMultipleChoiceField(
        queryset=MultiMovieSet.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Movie
        fields = ['title', 'year', 'multi_movie_sets']

    def clean_year(self):
        year = self.cleaned_data['year']
        try:
            year_datetime = movie_year_factory(year)
        except ValueError:
            raise forms.ValidationError('Invalid year')
        return year_datetime
    