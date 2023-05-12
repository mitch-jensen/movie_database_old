from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView
from django.views import View
from movies.forms import MovieCreateForm
from movies.models import Movie


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
    form_class = MovieCreateForm
    success_url = '/movies/add'

