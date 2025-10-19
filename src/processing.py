from datetime import datetime
from typing import Any


def filter_by_state(my_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
       Функция фильтрует список словарей по ключу 'state'.
       :param my_list: список словарей, содержащих ключ 'state'
       :param state: статус фильтрации
       :return: отфильтрованный список
    """
    result = list(filter(lambda item: item.get("state") == state, my_list))
    return result


def sort_by_date(data: list[dict[str, Any]], ascending: bool = False) -> list[dict[str, Any]]:
    """
        Сортирует список словарей по ключу 'date'.

        :param data: список словарей, содержащих ключ 'date'
        :param ascending: порядок сортировки (по возрастанию, если True; по убыванию — по умолчанию)
        :return: новый отсортированный список
    """
    return sorted(
        data,
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d"),
        reverse=not ascending
    )
