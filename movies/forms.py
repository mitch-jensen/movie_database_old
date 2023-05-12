from django import forms

from .models import Movie, movie_year_factory


class MovieCreateForm(forms.ModelForm):
    title = forms.CharField()
    year = forms.IntegerField()

    class Meta:
        model = Movie
        fields = ['title', 'year']

    def clean_year(self):
        year = self.cleaned_data['year']
        try:
            year_datetime = movie_year_factory(year)
        except ValueError:
            raise forms.ValidationError('Invalid year')
        return year_datetime
    