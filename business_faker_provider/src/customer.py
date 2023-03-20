import random
from datetime import datetime

from faker.providers import BaseProvider


class CustomerProvider(BaseProvider):
    """Customer Provider."""

    __provider__ = "customer_full_name"
    __provider__ = "customer_date_of_birth"
    __provider__ = "customer_email_address"
    __provider__ = "customer_street_address"
    __provider__ = "customer_phone_number"
    __lang__ = "en_GB"

    def customer_fullname(self, as_str: bool = False):
        """Generate a Person full name.

        Args:
            as_str (bool): whether to return the value as a string

        Returns:
            dict: Person full name

        Example:
            {
                "first": "John",
                "last": "Doe",
                "title": "Mr"
            }
        """
        sex_ = self.random_element(["F", "M"])
        first = self.generator.first_name_male() if sex_ == "M" else self.generator.first_name_female()
        last = self.generator.last_name()
        title = self.generator.prefix_male() if sex_ == "M" else self.generator.prefix_female()

        if as_str:
            return f"{title.lower()} {first.lower()} {last.lower()}".title()

        return {
            "first": first,
            "last": last,
            "title": title,
        }

    def customer_date_of_birth(self, date_format: str = "%d-%m-%Y", allow_under_aged: bool = False) -> str:
        """Generate a date of birth.

        Args:
            date_format (str): date format. Defaults to "%d-%m-%Y".
            allow_under_aged (bool): can the date of birth be under 18? Defaults to False.

        Returns:
            str: date of birth
        """
        underaged = False

        if allow_under_aged:
            underaged = bool(random.getrandbits(1))

        date_of_birth = self.generator.date_of_birth() if underaged else self.generator.date_of_birth(minimum_age=18)

        return date_of_birth.strftime(date_format)

    def customer_email_address(self, first: str = None, last: str = None, domain: str = "yopmail.com") -> str:
        """Generate an email address.

        Args:
            first (str): first name. Defaults to "John".
            last (str): last name. Defaults to "Doe".

        Returns:
            str: email address

        Example:
            test-john.doe-20200101_120000@yopmail.com
        """
        first = first or self.generator.first_name()
        last = last or self.generator.last_name()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        domain = domain or self.generator.free_email_domain()

        return f"test-{first.lower()}.{last.lower()}-{timestamp}@{domain}"

    def customer_street_address(self, address_as_list: bool = True, postcode: str = None, full: bool = False) -> dict:
        """Generate a player address.

        Args:
            address_as_list (bool): address as list. Defaults to True.
            postcode (str): postcode. Defaults to None.
            full (bool): provide additional fields value (county and coutry_code)

        Returns:
            dict: player address

        Example:
            {
                "address": ["The Peoples Postcode Lottery", "28 Charlotte Square"],
                "town": "Edinburgh",
                "postcode": "EH2 4ET"
            }
        OR
            {
                "address": "The Peoples Postcode Lottery, 28 Charlotte Square",
                "town": "Edinburgh",
                "postcode": "EH2 4ET"
            }
            {
                "address": "The Peoples Postcode Lottery, 28 Charlotte Square",
                "town": "Edinburgh",
                "postcode": "EH2 4ET",
                "county": "Mid Lothian",
                "country_code": "GB
            }
        """
        street_address = self.generator.street_address()
        postcode = postcode or self.generator.postcode()
        street_address = street_address.split("\n") if address_as_list else street_address

        address = {"address": street_address, "town": self.generator.city(), "postcode": postcode}

        if full:
            address["county"] = self.generator.county()
            address["country_code"] = "GB"

        return address

    def customer_phone_number(self, is_mobile: bool = False, country_prefix: bool = False) -> str:
        """Generate a person phone number.

        Args:
            is_mobile (bool): phone number is for a mobile
            country_prefix (bool): include country prefix

        Returns:
            str: person phone number
        """

        prefix = "+44" if country_prefix else "0"

        if is_mobile:
            return f"{prefix}{self.generator.bothify(text='7#########')}"

        return f"{prefix}{self.generator.bothify(text='1#########')}"
