from datetime import datetime, timedelta

from ._request import ApiRequester
from .types import CurrencyType, RequestType
from ._utils import get_table
from ._exceptions import NotExistsError
from .models import Currency, Gold

from . import _urls
from . import _settings


class _NBPApiClientBase:
    def raw_request(self, url: str, type: RequestType, params: dict | None = None) -> dict | None:
        """
        Umozliwia bezposrednie odpytanie API
        """
        match type:
            case RequestType.GET:
                return ApiRequester(url=url).get(params=params)


class _NBPApiClientGoldPriceMixin(_NBPApiClientBase):
    def get_gold_rate_currently_valid(self) -> Gold | None:
        """
        Aktualnie obowiązująca cena złota
        """

        try:
            response = ApiRequester(
                url=_urls.LATEST_GOLD_RATE_URL
            ).get()
        except NotExistsError:
            return

        return Gold.from_response(response[0])

    def get_gold_rate_from_today(self) -> Gold | None:
        """
        Cena złota opublikowana w dniu dzisiejszym (albo brak danych)
        """
        try:
            response = ApiRequester(
                url=_urls.TODAY_GOLD_RATE_URL
            ).get()
        except NotExistsError:
            return
        
        return Gold.from_response(response[0])
    
    def get_gold_rate_from_date(self, date: datetime) -> Gold | None:
        """
        Cena złota opublikowana w dniu {date} (albo brak danych)
        """
        try:
            response = ApiRequester(
                url=_urls.GOLD_RATE_FROM_DATE_URL(date.strftime(_settings.DATE_FORMAT))
            ).get()
        except NotExistsError:
            return
        
        return Gold.from_response(response[0])

    def get_gold_rate_from_working_day_before_date(self, date: datetime) -> Gold:
        """
        Cena złota opublikowana w dniu roboczym poprzedzającym podaną datę {date}

        Jeśli podasz datę której dzień tygodnia wypada w poniedziałek, kurs zostanie pobrany z piątku.
        Jeśli podasz datę której dzień tygodnia wypada w środę, kurs zostanie pobrany z wtorku.
        """
        response = None
        before_date = date - timedelta(days=1)

        while True:
            try:
                response = ApiRequester(
                    url=_urls.GOLD_RATE_FROM_DATE_URL(
                        before_date.strftime(_settings.DATE_FORMAT)
                    )
                ).get()
            except NotExistsError:
                before_date = before_date - timedelta(days=1)
                continue
            else:
                break

        return Gold.from_response(response[0])

    def get_gold_rate_from_start_date_to_end_date(
            self,
            start_date: datetime,
            end_date: datetime
        ) -> list[Gold]:
        """
        Seria tabel kursów typu opublikowanych w zakresie dat od {start_date} do {end_date} (albo brak danych)
        """
        try:
            response = ApiRequester(
                url=_urls.GOLD_RATE_FROM_START_DATE_TO_END_DATE_URL(
                    start_date.strftime(_settings.DATE_FORMAT),
                    end_date.strftime(_settings.DATE_FORMAT)
                )
            ).get()
        except NotExistsError:
            return []
        
        return [Gold.from_response(gold) for gold in response]


class _NBPApiClientCurrencyMixin(_NBPApiClientBase):
    def get_currency_rate_currently_valid(
            self,
            currency: CurrencyType
        ) -> Currency | None:
        """
        Aktualnie obowiązujący kurs waluty w PLN
        """
        table = get_table(currency)

        try:
            response = ApiRequester(
                url=_urls.LATEST_CURRENCY_RATE_URL(table.value, currency.value)
            ).get()
        except NotExistsError:
            return

        return Currency.from_response(response["rates"][0], type=currency)

    def get_currency_rate_from_today(
            self,
            currency: CurrencyType
        ) -> Currency | None:
        """
        Kurs waluty w PLN opublikowany w dniu dzisiejszym (albo brak danych)
        """
        table = get_table(currency)

        try:
            response = ApiRequester(
                url=_urls.TODAY_CURRENCY_RATE_URL(table.value, currency.value)
            ).get()
        except NotExistsError:
            return

        return Currency.from_response(response["rates"][0], type=currency)
    
    def get_currency_rate_from_date(
            self,
            currency: CurrencyType,
            date: datetime
        ) -> Currency | None:
        """
        Kurs waluty opublikowany w dniu {date} (albo brak danych)
        """
        table = get_table(currency)

        try:
            response = ApiRequester(
                url=_urls.CURRENCY_RATE_FROM_DATE_URL(
                    table.value,
                    currency.value,
                    date.strftime(_settings.DATE_FORMAT)
                )
            ).get()
        except NotExistsError:
            return
    
        return Currency.from_response(response["rates"][0], type=currency)

    def get_currency_rate_from_working_day_before_date(
            self,
            currency: CurrencyType,
            date: datetime
        ) -> Currency:
        """
        Kurs waluty opublikowany w dniu roboczym poprzedzającym podaną datę {date}

        Jeśli podasz datę której dzień tygodnia wypada w poniedziałek, kurs zostanie pobrany z piątku.
        Jeśli podasz datę której dzień tygodnia wypada w środę, kurs zostanie pobrany z wtorku.
        """
        table = get_table(currency)

        response = None
        before_date = date - timedelta(days=1)

        while True:
            try:
                response = ApiRequester(
                    url=_urls.CURRENCY_RATE_FROM_DATE_URL(
                        table.value,
                        currency.value,
                        before_date.strftime(_settings.DATE_FORMAT)
                    )
                ).get()
            except NotExistsError:
                before_date = before_date - timedelta(days=1)
                continue
            else:
                break

        return Currency.from_response(response["rates"][0], type=currency)

    def get_currency_rate_from_start_date_to_end_date(
            self,
            currency: CurrencyType,
            start_date: datetime,
            end_date: datetime
        ) -> list[Currency]:
        """
        Seria tabel kursów typu opublikowanych w zakresie dat od {start_date} do {end_date} (albo brak danych)
        """
        table = get_table(currency)

        try:
            response = ApiRequester(
                url=_urls.CURRENCY_RATE_FROM_START_DATE_TO_END_DATE_URL(
                    table.value,
                    currency.value,
                    start_date.strftime(_settings.DATE_FORMAT),
                    end_date.strftime(_settings.DATE_FORMAT)
                )
            ).get()
        except NotExistsError:
            return []

        return [Currency.from_response(rate, type=currency) for rate in response["rates"]]


class NBPApiClient(
    _NBPApiClientCurrencyMixin,
    _NBPApiClientGoldPriceMixin
):
    pass