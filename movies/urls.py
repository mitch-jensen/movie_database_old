from django.urls import path

from movies.views import HomePageView, AboutPageView, MovieListView, DistributorListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("movies/", MovieListView.as_view(), name='all-movies'),
    path("distributors/", DistributorListView.as_view(), name='all-distributors'),
]
