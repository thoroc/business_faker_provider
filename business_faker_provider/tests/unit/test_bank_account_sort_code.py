import pytest


class TestBankAccountSortCode:
    @pytest.mark.repeat(5)
    def test_returns_str(self, faker):
        # Arrange
        sort_code = faker.bank_account_sort_code()

        # Assert
        assert isinstance(sort_code, str)
        assert sort_code != ""
        assert len(sort_code) == 6
