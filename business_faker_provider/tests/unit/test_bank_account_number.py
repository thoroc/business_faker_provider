import pytest


class TestBankAccountNumber:
    @pytest.mark.repeat(5)
    def test_returns_str(self, faker):
        # Arrange
        expected_len = 8

        # Act
        number = faker.bank_account_number()

        # Assert
        assert isinstance(number, str)
        assert number != ""
        assert len(number) == expected_len
