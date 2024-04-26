from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from domain.entities.category import Category as CategoryEntity


class Category(ABC):

    @abstractmethod
    async def create(self, category:CategoryEntity) -> None:
        pass

    @abstractmethod
    async def update(self, category:CategoryEntity) -> None:
        pass

    @abstractmethod
    async def delete(self, id:UUID) -> None:
        pass

    @abstractmethod
    async def get(self) -> List[CategoryEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id:UUID) -> CategoryEntity:
        pass