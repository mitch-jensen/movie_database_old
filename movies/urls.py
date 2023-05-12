from django.urls import path

from movies.views import HomePageView, AboutPageView, MovieListView, MovieCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("movies/", MovieListView.as_view(), name='movies'),
    path("movies/add", MovieCreateView.as_view(), name='movie-create'),
]
