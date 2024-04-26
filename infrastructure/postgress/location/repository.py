from typing import List
from uuid import UUID
from domain.repositories.location_repository import LocationRepository
from domain.entities.location import Location as LocationEntity, LocationReview
from domain.utils.error_handling import AppError
from infrastructure.postgress.connection import Database


class PostgressLocationRepository(LocationRepository):

    def __init__(self, database: Database):
        self.database = database

    async def create(self, entity: LocationEntity) -> None:
        await self.database.execute(
            """
                INSERT INTO 
                    location (id, name, latitude, longitude) 
                VALUES 
                    ($1, $2, $3, $4)

            """,
            entity.id,
            entity.name,
            entity.latitude,
            entity.longitude,
        )

    async def update(self, entity: LocationEntity) -> None:
        await self.database.execute(
            """
                UPDATE 
                    location 
                SET 
                    name = $2, latitude = $3, longitude = $4
                WHERE 
                    id = $1 

            """,
            entity.id,
            entity.name,
            entity.latitude,
            entity.longitude,
        )

    async def delete(self, id: UUID) -> None:
        await self.database.execute(
            """
                UPDATE 
                    location 
                SET 
                    deleted_at = now()
                WHERE 
                    id = $1 

            """,
            id,
        )

    async def get(self) -> List[LocationEntity]:
        results = await self.database.fetch_many(
            """
                SELECT 
                    *
                FROM 
                    location 
                WHERE 
                    deleted_at is null
            """
        )

        return [LocationEntity(**result) for result in results]

    async def get_by_id(self, id: UUID) -> LocationEntity:
        result = await self.database.fetch_one(
            """
                SELECT 
                    *
                FROM 
                    location 
                WHERE 
                    id = $1 
                    AND deleted_at is null
            """,
            id,
        )

        if result is None:
            raise AppError(detail="Location not found.", code=AppError.DATASOURCE_ERROR)

        return LocationEntity(**result)

    async def get_by_ids(self, ids: List[UUID]) -> List[LocationEntity]:
        results = await self.database.fetch_many(
            """
            SELECT 
                *
            FROM 
                location 
            WHERE 
                deleted_at IS NULL
                AND id = ANY($1)
            """,
            ids,
        )

        return [LocationEntity(**result) for result in results]

    async def create_review(self, entity: LocationReview) -> None:
        await self.database.execute(
            """
                INSERT INTO 
                    category_location (id, category_id, location_id, reviewed) 
                VALUES 
                    ($1, $2, $3, $4)
            """,
            entity.id,
            entity.category_id,
            entity.location_id,
            entity.reviewed,
        )

    async def get_recommendations(self) -> List[LocationReview]:
        #obtiene todos pares categoria-ubicacion que no se encuentran relacionados
        #en la basde de datos; y los limita a 10 registros
        results = await self.database.fetch_many(
            """
                SELECT NULL as id, c.id AS category_id, l.id AS location_id, NULL as reviewed
                FROM category c, location l
                WHERE (c.id, l.id) NOT IN (
                    SELECT cl.category_id, cl.location_id
                    FROM category_location cl
                ) 
                AND c.deleted_at is null AND l.deleted_at is null
                LIMIT 10
            """
        )
        if len(results) < 10:
            #solo si la anterior consulta retorna menos de 10 registros hacemos una busqueda 
            #de las categorias-ubicaciones que si se encuentran relacionadas pero que su fecha 
            #de revision fue hace mas de 1 mes, se limita a 10 registros para cubrir el caso 
            #que la anterior consulta no haya retornado nada
            results2 = await self.database.fetch_many(
                """
                    SELECT DISTINCT
                        ON (category_id) id,
                        category_id,
                        location_id,
                        reviewed
                    FROM category_location
                    WHERE
                        reviewed < CURRENT_DATE - INTERVAL '1 month'
                    ORDER BY category_id, reviewed DESC
                    LIMIT 10
                """
            )
            results.extend(results2)
        #se truncan los resultados a 10 registros; ya que consume menos recursos, haber consultado 
        #un maximo de 9 registros de mas que implementar select anidados en la consulta sql
        results = results[:10]

        return [LocationReview(**result) for result in results]
