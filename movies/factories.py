import factory

from movies.models import Director

class DirectorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Director

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
