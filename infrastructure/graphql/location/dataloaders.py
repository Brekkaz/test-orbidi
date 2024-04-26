import uuid

from typing import List
from infrastructure.graphql.location.objects import Location
from domain.repositories.location_repository import LocationRepository
from strawberry.dataloader import DataLoader


def create_location_data_loader(repository: LocationRepository):
    """
    Decorador para una inyeccion limpia del repositorio en el dataloader
    """
    async def load_location(keys) -> List[Location]:
        """
        Dataloader para carga en batch de ubicaciones
        """
        return await repository.get_by_ids(ids=[uuid.UUID(str(k)) for k in keys])

    return DataLoader(load_fn=load_location)
