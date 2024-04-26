from typing import List
from uuid import UUID

from domain.usecases.location_usecase import Location as ILocationUseCase
from domain.repositories.location_repository import LocationRepository
from domain.entities.location import Location as LocationEntity, LocationReview


class Location(ILocationUseCase):
    def __init__(self, repository: LocationRepository):
        self.repository = repository

    async def create(self, entity: LocationEntity) -> None:
        await self.repository.create(entity=entity)

    async def update(self, entity: LocationEntity) -> None:
        await self.repository.get_by_id(id=entity.id)
        await self.repository.update(entity=entity)

    async def delete(self, id: UUID) -> None:
        await self.repository.get_by_id(id=id)
        await self.repository.delete(id=id)

    async def get(self) -> List[LocationEntity]:
        return await self.repository.get()

    async def get_by_id(self, id: UUID) -> LocationEntity:
        return await self.repository.get_by_id(id=id)

    async def create_review(self, entity: LocationReview) -> None:
        await self.repository.create_review(entity=entity)

    async def get_recommendations(self) -> List[LocationReview]:
        return await self.repository.get_recommendations()
