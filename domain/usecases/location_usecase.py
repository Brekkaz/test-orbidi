from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from domain.entities.location import Location as LocationEntity


class Location(ABC):

    @abstractmethod
    async def create(self, location:LocationEntity) -> None:
        pass

    @abstractmethod
    async def update(self, location:LocationEntity) -> None:
        pass

    @abstractmethod
    async def delete(self, id:UUID) -> None:
        pass

    @abstractmethod
    async def get(self) -> List[LocationEntity]:
        pass

    @abstractmethod
    async def get_by_id(self, id:UUID) -> LocationEntity:
        pass