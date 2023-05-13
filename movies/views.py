from typing import Any, Optional, Type
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView
from django.views import View
from movies.forms import MovieCreateUpdateForm
from movies.models import Movie, MultiMovieSet


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'

class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movies/movie_add.html'
    form_class = MovieCreateUpdateForm
    success_url = '/movies/add'

class MovieUpdateView(UpdateView):
    model = Movie
    model = Movie
    template_name = 'movies/movie_add.html'
    form_class = MovieCreateUpdateForm
    success_url = '/movies'


class MultiMovieSetCreateView(CreateView):
    model = MultiMovieSet
    fields = ['title', 'movies']
    template_name = 'movies/multi_movie_set_add.html'
    success_url = '/movies/add/multi_movie_set'

    def get_form(self, form_class: Type[BaseModelForm] | None = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['movies'].required = False
        return form