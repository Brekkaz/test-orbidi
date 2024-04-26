from typing import List
from uuid import UUID

from domain.usecases.category_usecase import Category as ICategoryUseCase
from domain.repositories.category_repository import CategoryRepository
from domain.entities.category import Category as CategoryEntity


class Category(ICategoryUseCase):
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def create(self, entity: CategoryEntity) -> None:
        await self.repository.create(entity=entity)

    async def update(self, entity: CategoryEntity) -> None:
        await self.repository.get_by_id(id=entity.id)
        await self.repository.update(entity=entity)

    async def delete(self, id: UUID) -> None:
        await self.repository.get_by_id(id=id)
        await self.repository.delete(id=id)

    async def get(self) -> List[CategoryEntity]:
        return await self.repository.get()

    async def get_by_id(self, id: UUID) -> CategoryEntity:
        return await self.repository.get_by_id(id=id)
