import time
from datetime import datetime

from faker.providers import BaseProvider


class CommonProvider(BaseProvider):
    """Common data provider."""

    __provider__ = "date_now_utc"
    __lang__ = "en_GB"

    def date_now_utc(self) -> str:
        """Generate a timestamp.

        Returns:
          str: a datetime in the format YYYY-mm-ddTHH:MM:SS
        """
        now = int(time.time())

        return str(datetime.fromtimestamp(now).isoformat("T", "seconds"))
