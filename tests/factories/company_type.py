import factory
from factory.django import DjangoModelFactory

from core.apps.companies.models import CompanyType


class CompanyTypeModelFactory(DjangoModelFactory):
    title = factory.Faker('first_name')

    class Meta:
        model = CompanyType
