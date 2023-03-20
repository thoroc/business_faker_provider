import re

import pytest


class TestcustomerEmailAddress:
    @pytest.mark.repeat(5)
    def test_returns_str(self, faker):
        # Arrange
        pattern = re.compile(r"test\-[\w\.]+\-\d{8}_\d{6}@\w+\.\w{2,3}")

        # Act
        email = faker.customer_email_address()

        # Assert
        assert email is not None
        assert isinstance(email, str)
        assert email != ""
        assert "@" in email
        assert "yopmail" in email
        assert pattern.match(email) is not None

    @pytest.mark.repeat(5)
    def test_returns_str_first_name(self, faker):
        # Arrange
        first = faker.first_name()

        # Act
        email = faker.customer_email_address(first=first)

        # Assert
        assert first.lower() in email

    @pytest.mark.repeat(5)
    def test_returns_str_last_name(self, faker):
        # Arrange
        last = faker.last_name()

        # Act
        email = faker.customer_email_address(last=last)

        # Assert
        assert last.lower() in email

    @pytest.mark.repeat(5)
    def test_returns_str_domain(self, faker):
        # Arrange
        domain = faker.domain_name()

        # Act
        email = faker.customer_email_address(domain=domain)

        # Assert
        assert domain in email
