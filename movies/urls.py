from django.urls import path

from movies.views import HomePageView, AboutPageView, MovieListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("movies/", MovieListView.as_view(), name='all-movies'),
]
