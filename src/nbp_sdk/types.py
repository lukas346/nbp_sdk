from enum import Enum


class RequestType(Enum):
    GET = "GET"


class CurrencyType(Enum):
    USD = "USD"
    AUD = "AUD"
    HKD = "HKD"
    CAD = "CAD"
    SGD = "SGD"
    EUR = "EUR"
    CHF = "CHF"
    GBP = "GBP"
    JPY = "JPY"
    CZK = "CZK"
    NOK = "NOK"
    SEK = "SEK"
    KRW = "KRW"
    HUF = "HUF"
    BRL = "BRL"


class TableType(Enum):
    A = "A"
    B = "B"
    C = "C"
