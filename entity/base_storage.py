from typing import Dict

from entity.abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, name: str, amount: int) -> None:

        if self.get_free_space() < amount:
            pass


        self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:

        if name not in self._items:
            pass

        if self._items[name] < amount:
            ...


        self._items[name] -= amount


    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> Dict[str, int]:
        return self._items

    def get_uniqe_items_count(self) -> int:
        return len(self._items)


