from .types import CurrencyType, TableType


def get_table(currency: CurrencyType) -> TableType | None:
    mapper = {
        TableType.A: (
            CurrencyType.USD,
            CurrencyType.AUD,
            CurrencyType.HKD,
            CurrencyType.CAD,
            CurrencyType.SGD,
            CurrencyType.EUR,
            CurrencyType.CHF,
            CurrencyType.GBP,
            CurrencyType.JPY,
            CurrencyType.CZK,
            CurrencyType.NOK,
            CurrencyType.SEK,
            CurrencyType.KRW,
            CurrencyType.HUF,
            CurrencyType.BRL
        )
    }

    for table, currencies in mapper.items():
        if currency in currencies:
            return table
