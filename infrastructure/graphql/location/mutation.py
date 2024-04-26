import uuid
from uuid import UUID

import strawberry
from strawberry import ID
from strawberry.types import Info

from domain.utils.error_handling import AppError
from infrastructure.graphql.location.inputs import LocationInput, ReviewInput


@strawberry.type
class LocationMutation:

    @strawberry.mutation()
    async def location_create(self, info: Info, data: LocationInput) -> UUID:
        """
        Habilita la mutacion para crear ubicaciones
        """
        try:
            instance = data.to_pydantic().to_entity(id=uuid.uuid4())
            await info.context.location.create(entity=instance)
            return instance.id
        except AppError as e:
            raise e.extend()

    @strawberry.mutation()
    async def location_update(self, info: Info, id: ID, data: LocationInput) -> bool:
        """
        Habilita la mutacion para actualizar ubicaciones
        """
        try:
            instance = data.to_pydantic().to_entity(id=UUID(str(id)))
            await info.context.location.update(entity=instance)
            return True
        except AppError as e:
            raise e.extend()

    @strawberry.mutation()
    async def location_delete(self, info: Info, id: ID) -> bool:
        """
        Habilita la mutacion para eliminar ubicaciones
        """
        try:
            await info.context.location.delete(id=UUID(str(id)))
            return True
        except AppError as e:
            raise e.extend()

    @strawberry.mutation()
    async def review_create(self, info: Info, data: ReviewInput) -> UUID:
        """
        Habilita la mutacion para crear revisiones
        """
        try:
            instance = data.to_pydantic().to_entity(id=uuid.uuid4())
            await info.context.location.create_review(entity=instance)
            return instance.id
        except AppError as e:
            raise e.extend()
