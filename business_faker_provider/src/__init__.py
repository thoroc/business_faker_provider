from business_faker_provider.src.banking import BankingProvider
from business_faker_provider.src.common import CommonProvider
from business_faker_provider.src.customer import CustomerProvider


class BusinessProvider(BankingProvider, CommonProvider, CustomerProvider):
    """Wrapper Provider."""
