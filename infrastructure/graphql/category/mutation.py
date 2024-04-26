import uuid
from uuid import UUID

import strawberry
from strawberry import ID
from strawberry.types import Info

from domain.entities.category import Category
from domain.utils.error_handling import AppError
from infrastructure.graphql.category.inputs import CategoryInput


@strawberry.type
class CategoryMutation:

    @strawberry.mutation()
    async def category_create(self, info: Info, data: CategoryInput) -> UUID:
        """
        Habilita la mutacion para crear categorias
        """
        try:
            instance = data.to_pydantic().to_entity(id=uuid.uuid4())
            await info.context.category.create(entity=instance)
            return instance.id
        except AppError as e:
            raise e.extend()

    @strawberry.mutation()
    async def category_update(self, info: Info, id: ID, data: CategoryInput) -> bool:
        """
        Habilita la mutacion para actualizar categorias
        """
        try:
            instance = data.to_pydantic().to_entity(id=UUID(str(id)))
            await info.context.category.update(entity=instance)
            return True
        except AppError as e:
            raise e.extend()

    @strawberry.mutation()
    async def category_delete(self, info: Info, id: ID) -> bool:
        """
        Habilita la mutacion para eliminar categorias
        """
        try:
            await info.context.category.delete(id=UUID(str(id)))
            return True
        except AppError as e:
            raise e.extend()
