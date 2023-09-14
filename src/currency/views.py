from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from currency.models import Currency
from currency.serializers import CurrencySerializer
from currency.services import CurrencyIntegration


class CurrencyListAPIView(ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class CurrencyConverterAPIView(APIView):

    @extend_schema(
        description="Валюты надо вводить по типу [USD, RUB, EUR],"
                    "все типы можно посмотреть по адресу api/v1/currencies/",
        parameters=[
            OpenApiParameter(
                name="from_currency", location=OpenApiParameter.QUERY, description="from_currency",
                required=True, type=str, default="RUB"
            ),
            OpenApiParameter(
                name="to_currency", location=OpenApiParameter.QUERY, description="to_currency", required=True,
                type=str, default="USD"
            ),
            OpenApiParameter(
                name="amount", location=OpenApiParameter.QUERY, description="amount", required=False,
                type=int, default=1
            ),
        ],
        responses={201: OpenApiResponse(description='{"result": "0.0"}')}
    )
    def get(self, request, *args, **kwargs):
        converted_currencies = CurrencyIntegration.convert_currencies(amount=request.query_params.get("amount"),
                                                                      from_currency=request.query_params.get(
                                                                          "from_currency"),
                                                                      to_currency=request.query_params.get(
                                                                          "to_currency"))
        return Response(data=converted_currencies, status=status.HTTP_200_OK)
