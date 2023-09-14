from dataclasses import dataclass
from typing import Optional

import requests
from rest_framework.exceptions import ParseError


@dataclass
class BaseCurrencyIntegration:
    base_url: str
    timeout: int

    @classmethod
    def _get(cls, url: str, query_params: Optional[dict] = None, timeout: Optional[int] = None, ) -> requests.Response:
        try:
            response = requests.get(url=url, params=query_params, timeout=timeout)
            if response.ok:
                return response
        except requests.ConnectionError:
            raise ParseError()



