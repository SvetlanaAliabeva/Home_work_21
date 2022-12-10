from typing import Dict

from entity.base_storage import BaseStorage

class Store(BaseStorage):
    def __int__(self, items: Dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)

