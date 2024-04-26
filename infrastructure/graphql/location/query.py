from typing import List

import strawberry
from strawberry import ID
from strawberry.types import Info

from infrastructure.graphql.location.objects import Location, LocationReview
from domain.utils.error_handling import AppError
from datetime import datetime


@strawberry.type
class LocationQuery:

    @strawberry.field()
    async def locations(self, info: Info) -> List[Location]:
        """
        Habilita la query para listar las ubicaciones
        """
        try:
            results = await info.context.location.get()
            return [Location.from_entity(entity=location) for location in results]
        except AppError as e:
            raise e.extend()

    @strawberry.field()
    async def location(self, info: Info, id: ID) -> Location:
        """
        Habilita la query para consultar una ubicacion
        """
        try:
            location = await info.context.location.get_by_id(id=id)
            return Location.from_entity(entity=location)
        except AppError as e:
            raise e.extend()

    @strawberry.field()
    async def recommendations(self, info: Info) -> List[LocationReview]:
        """
        Habilita la query para obtener un listado de 10 recomendaciones a revisar
        """
        try:
            results = await info.context.location.get_recommendations()
            return [LocationReview.from_entity(entity=review) for review in results]
        except AppError as e:
            raise e.extend()
