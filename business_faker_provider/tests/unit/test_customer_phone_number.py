import pytest


class TestPersonPhoneNumber:
    @pytest.mark.repeat(5)
    def test_returns_str(self, faker):
        # Arrange
        min_length = 8
        max_length = 13

        # Act
        phone_number = faker.customer_phone_number()

        # Assert
        assert phone_number is not None
        assert isinstance(phone_number, str)
        assert phone_number != ""
        assert phone_number[0] == "0"
        assert min_length <= len(phone_number) <= max_length

    @pytest.mark.repeat(5)
    def test_returns_str_is_land_line(self, faker):
        # Act
        phone_number = faker.customer_phone_number()

        # Assert
        assert phone_number[1] == "1"

    @pytest.mark.repeat(5)
    def test_returns_str_is_mobile(self, faker):
        # Act
        phone_number = faker.customer_phone_number(is_mobile=True)

        # Assert
        assert phone_number[1] == "7"

    @pytest.mark.repeat(5)
    def test_returns_str_has_country_prefix(self, faker):
        # Act
        phone_number = faker.customer_phone_number(country_prefix=True)

        # Assert
        assert phone_number[0:3] == "+44"
