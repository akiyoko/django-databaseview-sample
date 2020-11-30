from datetime import datetime


def format_yen(value: int) -> str:
    if value is not None:
        return f'{value:,} 円'


def format_yyyy_gatsu_mm_nichi(value: datetime) -> str:
    if value is not None:
        return value.strftime('%Y月%m日')
