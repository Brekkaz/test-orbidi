from typing import List

from domain.repositories.category_repository import CategoryRepository
from domain.entities.category import Category as CategoryEntity
from domain.utils.error_handling import AppError
from infrastructure.postgress.connection import Database
from uuid import UUID


class PostgressCategoryRepository(CategoryRepository):

    def __init__(self, database: Database):
        self.database = database

    async def create(self, entity: CategoryEntity) -> None:
        await self.database.execute(
            """
                INSERT INTO 
                    category (id, name) 
                VALUES 
                    ($1, $2)

            """,
            entity.id,
            entity.name,
        )

    async def update(self, entity: CategoryEntity) -> None:
        await self.database.execute(
            """
                UPDATE 
                    category 
                SET 
                    name = $2
                WHERE 
                    id = $1 

            """,
            entity.id,
            entity.name,
        )

    async def delete(self, id: UUID) -> None:
        await self.database.execute(
            """
                UPDATE 
                    category 
                SET 
                    deleted_at = now()
                WHERE 
                    id = $1 

            """,
            id,
        )

    async def get(self) -> List[CategoryEntity]:
        results = await self.database.fetch_many(
            """
                SELECT 
                    *
                FROM 
                    category 
                WHERE 
                    deleted_at is null
            """
        )

        return [CategoryEntity(**result) for result in results]

    async def get_by_id(self, id: UUID) -> CategoryEntity:
        result = await self.database.fetch_one(
            """
                SELECT 
                    *
                FROM 
                    category 
                WHERE 
                    id = $1 
                    AND deleted_at is null
            """,
            id,
        )

        if result is None:
            raise AppError(detail="Category not found.", code=AppError.DATASOURCE_ERROR)

        return CategoryEntity(**result)

    async def get_by_ids(self, ids: List[UUID]) -> List[CategoryEntity]:
        results = await self.database.fetch_many(
            """
            SELECT 
                *
            FROM 
                category 
            WHERE 
                deleted_at IS NULL
                AND id = ANY($1)
            """,
            ids,
        )

        return [CategoryEntity(**result) for result in results]
