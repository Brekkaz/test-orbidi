from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from domain.entities.location import Location as LocationEntity, LocationReview


class Location(ABC):

    @abstractmethod
    async def create(self, location: LocationEntity) -> None:
        pass

    @abstractmethod
    async def update(self, location: LocationEntity) -> None:
        """
        Valida la existencia de una ubicacion y luego actualiza 
        su informacion.
        Args:
        location: ubicacion a actualizar.
        """
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        """
        Valida la existencia de una ubicacion y luego la marca 
        como eliminada(soft delete).
        Args:
        id: identificador de la ubicacion a eliminar.
        """
        pass

    @abstractmethod
    async def get(self) -> List[LocationEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> LocationEntity:
        pass

    @abstractmethod
    async def create_review(self, entity: LocationReview) -> None:
        pass

    @abstractmethod
    async def get_recommendations(self) -> List[LocationReview]:
        pass
