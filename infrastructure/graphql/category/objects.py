import strawberry

from strawberry import ID
from domain.entities.category import Category as CategoryEntity


@strawberry.type
class Category:
    """
    Parsea la salida de la entidad categoria
    """
    id: ID
    name: str

    @staticmethod
    def from_entity(entity: CategoryEntity) -> "Category":
        return Category(id=ID(str(entity.id)), name=entity.name)
