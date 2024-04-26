from typing import List
from uuid import UUID

from domain.usecases.location_usecase import Location as ILocationUseCase
from domain.repositories.location_repository import LocationRepository
from domain.entities.location import Location as LocationEntity


class Location(ILocationUseCase):
    def __init__(self, repository: LocationRepository):
        self.repository = repository

    async def create(self, category:LocationEntity) -> None:
        await self.repository.create(entity=category)

    async def update(self, category:LocationEntity) -> None:
        pass
        #await self.repository.create_ad(entity=entity)

    async def delete(self, id:UUID) -> None:
        pass
        #await self.repository.create_ad(entity=entity)

    async def get(self) -> List[LocationEntity]:
        pass
        #await self.repository.create_ad(entity=entity)

    async def get_by_id(self, id:UUID) -> LocationEntity:
        pass
        #await self.repository.create_ad(entity=entity)
