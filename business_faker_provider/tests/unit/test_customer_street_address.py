import re

import pytest


class TestcustomerStreetAddress:
    @pytest.mark.repeat(5)
    def test_returns_dict_has_address(self, faker):
        # Arrange
        address = faker.customer_street_address()

        # Assert
        assert isinstance(address, dict)
        assert "address" in address.keys()
        assert isinstance(address["address"], list)
        assert address["address"] != []

    @pytest.mark.repeat(5)
    def test_returns_dict_has_address_as_str(self, faker):
        # Arrange
        address = faker.customer_street_address(address_as_list=False)

        # Assert
        assert isinstance(address, dict)
        assert "address" in address.keys()
        assert isinstance(address["address"], str)
        assert address["address"] != ""

    @pytest.mark.repeat(5)
    def test_returns_dict_has_town(self, faker):
        # Arrange
        address = faker.customer_street_address()

        # Assert
        assert isinstance(address, dict)
        assert "town" in address.keys()
        assert isinstance(address["town"], str)
        assert address["town"] != ""

    @pytest.mark.repeat(5)
    def test_returns_dict_has_postcode(self, faker):
        # Arrange
        address = faker.customer_street_address()
        pattern = re.compile(r"^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$")

        # Assert
        assert isinstance(address, dict)
        assert "postcode" in address.keys()
        assert isinstance(address["postcode"], str)
        assert address["postcode"] != ""

        postcode = address["postcode"].replace(" ", "")
        assert pattern.match(postcode)

    @pytest.mark.repeat(5)
    def test_returns_dict_specify_postcode(self, faker):
        # Arrange
        postcode = "SW1A 1AA"

        # Act
        address = faker.customer_street_address(postcode=postcode)

        # Assert
        assert address["postcode"] == postcode

    @pytest.mark.repeat(5)
    def test_returns_dict_without_none(self, faker):
        # Arrange
        address = faker.customer_street_address()

        # Assert
        assert not (None in address.values())

    @pytest.mark.repeat(5)
    def test_returns_dict_has_county(self, faker):
        # Arrange
        address = faker.customer_street_address(full=True)

        # Assert
        assert address["county"]

    @pytest.mark.repeat(5)
    def test_returns_dict_has_country_code(self, faker):
        # Arrange
        address = faker.customer_street_address(full=True)

        # Assert
        assert address["country_code"]
