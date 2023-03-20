from datetime import datetime

import arrow
import pytest


class TestcustomerDateOfBirth:
    def test_returns_str(self, faker):
        # Arrange
        date_of_birth = faker.customer_date_of_birth()

        # Assert
        assert date_of_birth is not None
        assert isinstance(date_of_birth, str)
        assert date_of_birth != ""

    def test_returns_str_date_format(self, faker):
        # Arrange
        date_of_birth = faker.customer_date_of_birth(date_format="%Y-%m-%d")

        # Assert
        assert bool(datetime.strptime(date_of_birth, "%Y-%m-%d"))

    @pytest.mark.repeat(5)
    def test_returns_str_not_underaged(self, faker):
        # Arrange
        date_of_birth = faker.customer_date_of_birth(allow_under_aged=False)

        # Act
        actual = arrow.get(date_of_birth, "DD-MM-YYYY")
        eighteen_years_ago = arrow.now().shift(years=-18)

        # Assert
        assert actual.date() < eighteen_years_ago.date()

    @pytest.mark.repeat(5)
    def test_returns_str_can_be_underaged(self, faker):
        # Arrange
        date_of_birth = faker.customer_date_of_birth(allow_under_aged=False)

        # Act
        actual = arrow.get(date_of_birth, "DD-MM-YYYY")
        now = arrow.now()

        # Assert
        assert actual.date() < now.date()
