from typing import List

from abc import ABC, abstractmethod
from domain.entities.category import Category as CategoryEntity
from uuid import UUID

class CategoryRepository(ABC):
    @abstractmethod
    async def create(self, entity: CategoryEntity) -> None:
        pass

    @abstractmethod
    async def update(self, entity: CategoryEntity) -> None:
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        pass

    @abstractmethod
    async def get(self) -> List[CategoryEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> CategoryEntity:
        pass