from typing import List

from domain.repositories.location_repository import LocationRepository
from domain.entities.location import Location as LocationEntity
from infrastructure.postgress.location.models import LocationModel
from domain.utils.error_handling import AppError
from infrastructure.postgress.connection import Database


class PostgressLocationRepository(LocationRepository):

    def __init__(self, database: Database):
        self.database = database

    async def create(self, entity: LocationEntity) -> None:
        await self.database.execute(
            """
                INSERT INTO 
                    location (id, name) 
                VALUES 
                    ($1, $2)

            """,
            entity.id, entity.name
        )

    async def update(self):
        pass

    async def delete(self):
        pass

    async def get(self):
        pass

    async def get_by_id(self):
        pass
