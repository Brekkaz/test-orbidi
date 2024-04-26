from typing import List

from uuid import UUID
from abc import ABC, abstractmethod
from domain.entities.location import Location as LocationEntity, LocationReview


class LocationRepository(ABC):
    @abstractmethod
    async def create(self, entity: LocationEntity) -> None:
        pass

    @abstractmethod
    async def update(self) -> None:
        pass

    @abstractmethod
    async def delete(self) -> None:
        pass

    @abstractmethod
    async def get(self) -> List[LocationEntity]:
        pass

    @abstractmethod
    async def get_by_id(self) -> LocationEntity:
        pass

    @abstractmethod
    async def get_by_ids(self, ids: List[UUID]) -> List[LocationEntity]:
        """
        Ejecuta una busqueda en la base de datos de todas las ubicaciones 
        que su id coincida con una lista de ids especificada.\n
        Args:
        ids: lista de ids a buscar.
        """
        pass

    @abstractmethod
    async def create_review(self, entity: LocationReview) -> None:
        """
        Crea una relacion entre una categoria y una ubicacion en la base de datos.\n
        Args:
        entity:
            id: identificador unico del nuevo registro
            category_id: identificador de la categoria
            location_id: identificador de la ubicacion
            reviewed: fecha y hora actual.
        """
        pass

    @abstractmethod
    async def get_recommendations(self) -> List[LocationReview]:
        """
        Obtiene de la base de datos un listado de 10 sugerencias de duplas categoria-ubicacion;
        priorizando las que no tienen un registro que las vincule y seguido de las existentes 
        pero que su ultima revision fue hace mas de un mes.
        """
        pass
