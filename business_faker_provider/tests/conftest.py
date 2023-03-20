import random

import pytest
from faker import Faker

from business_faker_provider.src import BusinessProvider


@pytest.fixture(scope="session")
def faker():
    _faker = Faker("en_GB")
    _faker.add_provider(BusinessProvider)
    seed = random.randint(10001, 99999)
    _faker.seed_instance(seed)

    return _faker
