import pytest
from movies.factories import DirectorFactory

class TestPhysicalMedia:
    def test_medium(self):
        assert 1 == 1

class TestDistributor:
    def test_distributor(self):
        assert 1 == 1

class TestCollection:
    def test_collection(self):
        assert 1 == 1

class TestMovie:
    def test_movie(self):
        assert 1 == 1

class TestDirector:
    @pytest.mark.django_db
    def test_str_method(self):
        director = DirectorFactory()
        assert str(director) == director.first_name + ' ' + director.last_name
