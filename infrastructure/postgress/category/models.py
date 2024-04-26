from uuid import UUID

from pydantic import BaseModel

from domain.entities.category import Category 


class CategoryModel(BaseModel):
    id: UUID
    name: str

    def to_entity(self) -> Category:
        return Category(
            id=self.id,
            name=self.name,
        )
