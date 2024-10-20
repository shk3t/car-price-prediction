from typing import Any, Collection

from library.typipng.typevar import T


def is_specified(value):
    return value or isinstance(value, (bool, int, float, str))


def flatten(nested_collection: Collection[Collection[T]]) -> list[T]:
    "Разворачивает вложенную коллекцию в плоский список"
    return [x for l in nested_collection for x in l]


def nonnone_dict(**data) -> dict:
    "Очищает словарь от записей с `None` и `[]`"
    return {
        k: v for k, v in data.items() if v or isinstance(v, (bool, int, float, str))
    }


def kv_swap(data: dict) -> dict:
    "Меняет местами ключи и значения в словаре"
    return {v: k for k, v in data.items()}


def discard(collection: set, key: Any) -> bool:
    "Удаляет элемент из сета и возвращает `True`, если удаление прошло успешно"
    try:
        collection.remove(key)
        return True
    except KeyError:
        return False
