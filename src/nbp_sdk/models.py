from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

from . import _settings


@dataclass
class Currency:
    # przeliczony kurs średni waluty
    average_rate: Decimal
    table_no: str
    # data publikacji
    effective_date: datetime

    @classmethod
    def from_response(cls, d: dict):
        return cls(
            average_rate=Decimal(str(d["mid"])),
            effective_date=datetime.strptime(d["effectiveDate"], _settings.DATE_FORMAT),
            table_no=d["no"]
        )


@dataclass
class Gold:
    # wyliczona w NBP cena 1 g złota (w próbie 1000)
    rate_per_1g: Decimal
    # data publikacji
    effective_date: datetime

    @classmethod
    def from_response(cls, d: dict):
        return cls(
           rate_per_1g=Decimal(str(d["cena"])),
           effective_date=datetime.strptime(d["data"], _settings.DATE_FORMAT), 
        )
