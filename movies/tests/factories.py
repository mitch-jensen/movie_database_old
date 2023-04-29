import factory
import random
from datetime import date

from movies.models import Director, Movie, Distributor


class DistributorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Distributor

    name = random.choice(Distributor.Studio.choices)[0]


class DirectorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Director

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    title = factory.Faker('sentence', nb_words=4, variable_nb_words=True)
    release_date = factory.Faker(
        'date_between_dates',
        date_start=date(1890, 1, 1),
        date_end=date.today()
    )
    watched = random.choice([True, False])

    @factory.post_generation
    def director(self, create, extracted, **kwargs):
        if not create:
            # Do nothing
            return

        if extracted:
            # A list of directors were passed in
            for director in extracted:
                self.director.add(director)
