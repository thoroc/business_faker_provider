class TestcustomerFullName:
    def test_returns_dict_has_title(self, faker):
        # Act
        actual = faker.customer_fullname()

        # Assert
        assert "title" in actual.keys()
        assert isinstance(actual["title"], str)

    def test_returns_dict_has_first(self, faker):
        # Act
        actual = faker.customer_fullname()

        # Assert
        assert "first" in actual.keys()
        assert isinstance(actual["first"], str)

    def test_returns_dict_has_last(self, faker):
        # Act
        actual = faker.customer_fullname()

        # Assert
        assert "last" in actual.keys()
        assert isinstance(actual["last"], str)

    def test_returns_str(self, faker):
        # Act
        actual = faker.customer_fullname(as_str=True)

        # Assert
        assert actual is not None
        assert isinstance(actual, str)
        assert actual != ""
