from typing import Any, Iterable
import re


def filter_query(value: str, data: Iterable[str]) -> filter:
    return filter(lambda x: value in x, data)

def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> set:
    return set(data)

def limit_query(value: str, data: Iterable[str]) -> list:
    limit: int = int(value)
    return list(data)[:limit]

def map_query(value: str, data: Iterable[str]) -> map:
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)

def sort_query(value: str, data: Iterable[str]) -> Iterable[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)

def regex(value: str, data: Iterable[str]) -> filter:
    reg = re.compile(value)
    return filter(lambda x: re.search(reg, x), data)

