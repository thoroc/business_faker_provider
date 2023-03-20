import re

import pytest


class TestCommonDateNowUtc:
    @pytest.mark.repeat(5)
    def test_returns_str(self, faker):
        # Arrange
        pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")

        # Act
        updated_utc = faker.date_now_utc()

        # Assert
        assert isinstance(updated_utc, str)
        assert pattern.match(updated_utc) is not None
