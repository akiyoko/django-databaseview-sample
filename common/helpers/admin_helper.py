from datetime import datetime


def format_yen(value: int) -> str:
    if value is not None:
        return f'{value:,} 円'


def format_yyyy_nen_mm_gatsu(value: datetime) -> str:
    if value is not None:
        return value.strftime('%Y年%m月')
