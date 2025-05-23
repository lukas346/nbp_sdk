# NBP SDK

[![Python package](https://github.com/lukas346/nbp_sdk/actions/workflows/python-package.yml/badge.svg)](https://github.com/lukas346/nbp_sdk/actions/workflows/python-package.yml)
[![PyPI version](https://badge.fury.io/py/nbp-sdk.svg)](https://badge.fury.io/py/nbp-sdk)
[![PyPI Downloads](https://static.pepy.tech/badge/nbp-sdk)](https://pepy.tech/projects/nbp-sdk)

SDK umozliwijące komunikację z [API Narodowego Banku Polskiego](http://api.nbp.pl).

![](https://ocdn.eu/pulscms-transforms/1/vPek9kpTURBXy9iNzhiN2YwZDU3OWZkODhiZjA1ODdiYTE1NDNlYTcxMy5qcGeSlQLNA8AAwsOVAgDNA8DCw94AAaEwAQ)

----------

Jeśli projekt ci się do czegoś przydał [to postaw mi kawę ☕](https://buycoffee.to/lukas346). Nie musi być to kawa z Starbucksa, taka biedronkowa też jest ok ;) Każda nawet najmniejsza dotacja to sygnał że to co robię jest dla was wartościowe i warto to utrzymywać.

## Instalacja

```bash
pip install nbp_sdk
```

## Poradniki
 * [PIT z Binance w 5 minut dzięki Pythonowi](https://www.whileforloop.pl/posts/pit-binance/)

## Przykładowe uzycie

```python
from nbp_sdk.client import NBPApiClient
from nbp_sdk.types import CurrencyType

api = NBPApiClient() 

currency = api.get_currency_rate_from_today(CurrencyType.EUR)
print(currency)

start_date = datetime(2024, 3, 11)
end_date = datetime(2024, 3, 14) 
currencies = api.get_currency_rate_from_start_date_to_end_date(CurrencyType.EUR, start_date, end_date)
print(currencies)

```

```python
from nbp_sdk.client import NBPApiClient

api = NBPApiClient() 

gold = api.get_gold_rate_currently_valid()
print(gold)

date = datetime(2024, 3, 14)
gold = api.get_gold_rate_from_working_day_before_date(date)
print(gold)

start_date = datetime(2024, 3, 11)
end_date = datetime(2024, 3, 14) 
golds = api.get_gold_rate_from_start_date_to_end_date(start_date, end_date)
print(golds)
```


W razie wątpliwości przeczytaj README do końca i rzuć okiem na [testy](https://github.com/lukas346/nbp_sdk/blob/main/tests/test_client.py).


## Dokumentacja

### Dostępne metody

---

    get_currency_rate_currently_valid

Aktualnie obowiązujący kurs waluty w PLN

    get_currency_rate_from_today

Kurs waluty w PLN opublikowany w dniu dzisiejszym (albo brak danych)

    get_currency_rate_from_date

Kurs waluty opublikowany w dniu {date} (albo brak danych)

    get_currency_rate_from_working_day_before_date

Kurs waluty opublikowany w dniu roboczym poprzedzającym podaną datę {date}

Jeśli podasz datę której dzień tygodnia wypada w poniedziałek, kurs zostanie pobrany z piątku.
Jeśli podasz datę której dzień tygodnia wypada w środę, kurs zostanie pobrany z wtorku.

    get_currency_rate_from_start_date_to_end_date

Seria tabel kursów typu opublikowanych w zakresie dat od {start_date} do {end_date} (albo brak danych)

---

    get_gold_rate_currently_valid

Aktualnie obowiązująca cena złota

    get_gold_rate_from_today

Cena złota opublikowana w dniu dzisiejszym (albo brak danych)

    get_gold_rate_from_date

Cena złota opublikowana w dniu {date} (albo brak danych)

    get_gold_rate_from_working_day_before_date

Cena złota opublikowana w dniu roboczym poprzedzającym podaną datę {date}

Jeśli podasz datę której dzień tygodnia wypada w poniedziałek, kurs zostanie pobrany z piątku.
Jeśli podasz datę której dzień tygodnia wypada w środę, kurs zostanie pobrany z wtorku.

    get_gold_rate_from_start_date_to_end_date
    
Seria tabel kursów typu opublikowanych w zakresie dat od {start_date} do {end_date} (albo brak danych)

### Zwracane modele
```python
class Currency:
    type: CurrencyType
    # przeliczony kurs średni waluty
    average_rate: Decimal
    table_no: str
    # data publikacji
    effective_date: datetime


class Gold:
    # wyliczona w NBP cena 1 g złota (w próbie 1000)
    rate_per_1g: Decimal
    # data publikacji
    effective_date: datetime
```

## Kontakt

Jeśli będzie Wam czegoś brakowało to dodajcie swoje Issue albo PR, które są oczywiście mile widziane.
