from django.urls import path

from currency.views import CurrencyListAPIView, CurrencyConverterAPIView

urlpatterns = [
    path("", CurrencyListAPIView.as_view(), name="currency-list"),
    path("convert/", CurrencyConverterAPIView.as_view(), name="currency-convert")
]