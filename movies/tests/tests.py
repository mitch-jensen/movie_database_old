import pytest
from .factories import DirectorFactory, MovieFactory, DistributorFactory
from movies.models import Distributor

class TestPhysicalMedia:
    def test_medium(self):
        assert 1 == 1


class TestCollection:
    def test_collection(self):
        assert 1 == 1

class TestDistributor:
    @pytest.mark.django_db
    def test_str_method(self):
        distributor = DistributorFactory()
        assert str(distributor) == Distributor.Studio(distributor.name).label

class TestMovie:
    @pytest.mark.django_db
    def test_str_method(self):
        movie = MovieFactory()
        assert str(movie) == movie.title + ' (' + str(movie.release_date.year) + ')'

class TestDirector:
    @pytest.mark.django_db
    def test_str_method(self):
        director = DirectorFactory()
        assert str(director) == director.first_name + ' ' + director.last_name
