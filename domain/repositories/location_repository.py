from abc import ABC, abstractmethod
from domain.entities.location import Location as LocationEntity

class LocationRepository(ABC):
    @abstractmethod
    async def create(self, entity: LocationEntity) -> None:
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    async def delete(self):
        pass

    @abstractmethod
    async def get(self):
        pass

    @abstractmethod
    async def get_by_id(self):
        pass