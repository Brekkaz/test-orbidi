import uuid

from typing import List
from infrastructure.graphql.category.objects import Category
from domain.repositories.category_repository import CategoryRepository
from strawberry.dataloader import DataLoader


def create_category_data_loader(repository: CategoryRepository):
    """
    Decorador para una inyeccion limpia del repositorio en el dataloader
    """
    async def load_categories(keys) -> List[Category]:
        """
        Dataloader para carga en batch de categorias
        """
        return await repository.get_by_ids(ids=[uuid.UUID(str(k)) for k in keys])

    return DataLoader(load_fn=load_categories)
