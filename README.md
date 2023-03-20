# Business related data Faker Provider

Provider for [Faker](https://faker.readthedocs.io/en/master/) to generate random/fake data related to Business data

## Requirements
* Faker
* Python
  

## Installation and Usage

If you want to use `business-faker-provider` within you project, add it to your dependency file of choice.

This is typically your project's `requirements.txt` file. If you are using a higher-level package manager like `poetry` or `pipenv`, follow their instructions for adding new packages.

Once, installed, you need to setup `Faker` to make use of the `PplProvider`. An example of how that could be done is shown below:
```python
from faker import Faker
from faker import Faker

from business_faker_provider.src import BusinessProvider

fake = Faker()
faker.add_provider(BusinessProvider)

fake.customer_fullname()
```

## Developing
* Install `poetry` and run `poetry install`

## Testing
* Run tests: `poetry run pytest`
* Run coverage: `poetry run coverage run -m pytest && poetry run coverage report -m --no-skip-covered`
* Format code: `poetry run black business_faker_provider`
* Sort imports: `poetry run isort business_faker_provider`