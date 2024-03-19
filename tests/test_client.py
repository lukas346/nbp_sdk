from unittest import TestCase
from datetime import datetime, timedelta

from src.nbp_sdk.client import NBPApiClient
from src.nbp_sdk.types import CurrencyType


class TestGoldNBPApiClient(TestCase):
    def setUp(self):
        self.api = NBPApiClient()

    # def test_gold_simple(self):
    #     assert self.api.get_gold_rate_currently_valid()
    #     assert self.api.get_gold_rate_from_today()


    def test_gold_rate_from_date(self):
        date = datetime(2024, 3, 14)
 
        gold = self.api.get_gold_rate_from_date(date)
        assert gold
        assert gold.effective_date == date

    def test_gold_rate_from_working_day_before_date(self):
        date_monday = datetime(2024, 3, 18)

        gold = self.api.get_gold_rate_from_working_day_before_date(date_monday)
        assert gold
        assert gold.effective_date == date_monday - timedelta(days=3)

    def test_gold_rate_from_start_date_to_end_date__weekend(self):
        start_date = datetime(2024, 3, 14)
        end_date = datetime(2024, 3, 17) 
        golds = self.api.get_gold_rate_from_start_date_to_end_date(start_date, end_date)
        assert len(golds) == 2

        for index, gold in enumerate(golds):
            assert gold.effective_date == start_date + timedelta(days=index)

    def test_gold_rate_from_start_date_to_end_date(self):
        start_date = datetime(2024, 3, 11)
        end_date = datetime(2024, 3, 14) 
        golds = self.api.get_gold_rate_from_start_date_to_end_date(start_date, end_date)
        assert len(golds) == 4

        for index, gold in enumerate(golds):
            assert gold.effective_date == start_date + timedelta(days=index)


class TestCurrenciesNBPApiClient(TestCase):
    def setUp(self):
        self.api = NBPApiClient()

    # def test_currency_simple(self):
    #     assert self.api.get_currency_rate_currently_valid(CurrencyType.USD)
    #     assert self.api.get_currency_rate_from_today(CurrencyType.EUR)

    def test_currenct_rate_from_date(self):
        date = datetime(2024, 3, 14)
 
        currency = self.api.get_currency_rate_from_date(CurrencyType.USD, date)
        assert currency
        assert currency.effective_date == date

    def test_currency_rate_from_working_day_before_date(self):
        date_monday = datetime(2024, 3, 18)

        currency = self.api.get_currency_rate_from_working_day_before_date(CurrencyType.USD, date_monday)
        assert currency
        assert currency.effective_date == date_monday - timedelta(days=3)

    def test_currency_rate_from_start_date_to_end_date__weekend(self):
        start_date = datetime(2024, 3, 14)
        end_date = datetime(2024, 3, 17) 
        currencies = self.api.get_currency_rate_from_start_date_to_end_date(CurrencyType.USD, start_date, end_date)
        assert len(currencies) == 2

        for index, currency in enumerate(currencies):
            assert currency.effective_date == start_date + timedelta(days=index)

    def test_currency_rate_from_start_date_to_end_date(self):
        start_date = datetime(2024, 3, 11)
        end_date = datetime(2024, 3, 14) 
        currencies = self.api.get_currency_rate_from_start_date_to_end_date(CurrencyType.AUD, start_date, end_date)
        assert len(currencies) == 4

        for index, currency in enumerate(currencies):
            assert currency.effective_date == start_date + timedelta(days=index)
