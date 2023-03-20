import pytest


class TestBankAccountNumber:
    @pytest.mark.repeat(5)
    def test_returns_str(self, faker):
        # Arrange
        number = faker.bank_account_number()

        # Assert
        assert isinstance(number, str)
        assert number != ""
        assert len(number) == 8
