from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView
from django.views import View
from movies.models import Movie


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class MovieBaseView(View):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:all-movies')


class MovieListView(MovieBaseView, ListView):
    pass
