from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from domain.entities.category import Category as CategoryEntity


class Category(ABC):

    @abstractmethod
    async def create(self, category: CategoryEntity) -> None:
        pass

    @abstractmethod
    async def update(self, category: CategoryEntity) -> None:
        """
        Valida la existencia de una categoria y luego actualiza 
        su informacion.
        Args:
        category: categoria a actualizar.
        """
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        """
        Valida la existencia de una categoria y luego la marca 
        como eliminada(soft delete).
        Args:
        id: identificador de la categoria a eliminar.
        """
        pass

    @abstractmethod
    async def get(self) -> List[CategoryEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> CategoryEntity:
        pass
