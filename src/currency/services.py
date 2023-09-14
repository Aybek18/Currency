from dataclasses import dataclass

from django.conf import settings

from core.services import BaseCurrencyIntegration


@dataclass
class CurrencyIntegration(BaseCurrencyIntegration):
    base_url = settings.INTEGRATION_BASE_URL
    timeout = settings.INTEGRATION_TIMEOUT

    @classmethod
    def convert_currencies(cls, from_currency: str, to_currency: str, amount: float):
        url = f"{cls.base_url}/convert?from={from_currency}&to={to_currency}&amount={amount}"
        response = cls._get(url=url, timeout=cls.timeout)
        return {"result": response.json()['result']}
