from django.urls import path

from movies.views import HomePageView, AboutPageView, MovieListView, MovieCreateView, MovieUpdateView, MultiMovieSetCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("movies/", MovieListView.as_view(), name='movies'),
    path("movies/add", MovieCreateView.as_view(), name='movie-create'),
    path("movies/update/<int:pk>", MovieUpdateView.as_view(), name='movie-update'),
    path("movies/add/multi_movie_set", MultiMovieSetCreateView.as_view(), name='multi-movie-set-create'),
]
