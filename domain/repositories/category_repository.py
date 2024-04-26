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

    @abstractmethod
    async def get_by_ids(self, ids: List[UUID]) -> List[CategoryEntity]:
        """
        Ejecuta una busqueda en la base de datos de todas las categorias 
        que su id coincida con una lista de ids especificada.\n
        Args:
        ids: lista de ids a buscar.
        """
        pass
