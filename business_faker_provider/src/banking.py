from faker.providers import BaseProvider


class BankingProvider(BaseProvider):
    """Banking Provider."""

    __provider__ = "bank_account_number"
    __provider__ = "bank_account_sort_code"
    __lang__ = "en_GB"

    def bank_account_number(self) -> str:
        """Generate a bank account number.

        Returns:
            str: The bank account number

        Example:
            "12345678"
        """
        iban = self.generator.iban()
        account_number = iban[14:22]

        return account_number

    def bank_account_sort_code(self) -> str:
        """Generate a bank account sort code.

        Returns:
            str: The bank account sort code

        Example:
            "123456"
        """
        iban = self.generator.iban()
        sort_code = iban[8:14]

        return sort_code
