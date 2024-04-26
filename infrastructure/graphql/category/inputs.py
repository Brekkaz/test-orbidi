import strawberry

from pydantic import BaseModel, Field
from domain.entities.category import Category
from uuid import UUID


class CategoryObject(BaseModel):
    """
    Valida y parsea la entrada de categorias
    """
    name: str = Field(min_length=3, max_length=100)

    def to_entity(self, id: UUID):
        return Category(id=id, name=self.name)


@strawberry.experimental.pydantic.input(model=CategoryObject, all_fields=True)
class CategoryInput:
    pass
