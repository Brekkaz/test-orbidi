import strawberry
from typing import Optional

from strawberry import ID
from datetime import datetime
from domain.entities.location import (
    Location as LocationEntity,
    LocationReview as LocationReviewEntity,
)
from infrastructure.graphql.category.objects import Category
from strawberry.types import Info


@strawberry.type
class Location:
    """
    Parsea la salida de la entidad location
    """
    id: ID
    name: str
    latitude: float
    longitude: float

    @staticmethod
    def from_entity(entity: LocationEntity) -> "Location":
        return Location(
            id=ID(str(entity.id)),
            name=entity.name,
            latitude=entity.latitude,
            longitude=entity.longitude,
        )


async def get_category(root: "LocationReview", info: Info) -> Category:
    """
    Resuelve la propiedad categoria haciendo uso de un dataloader
    """
    return await info.context.categories_loader.load(root.category_id)


async def get_location(root: "LocationReview", info: Info) -> Location:
    """
    Resuelve la propiedad location haciendo uso de un dataloader
    """
    return await info.context.location_loader.load(root.location_id)


@strawberry.federation.type(keys=["id", "category_id", "location_id"])
class LocationReview:
    """
    Parsea la salida de la entidad locationreview
    """
    id: Optional[ID]
    category_id: ID
    location_id: ID
    reviewed: Optional[datetime]
    category: Category = strawberry.field(resolver=get_category)#habilita federation para resolver la propiedad category
    location: Location = strawberry.field(resolver=get_location)#habilita federation para resolver la propiedad location

    @staticmethod
    def from_entity(entity: LocationReviewEntity) -> "LocationReview":
        id = ID(str(entity.id)) if entity.id is not None else None
        return LocationReview(
            id=id,
            category_id=ID(str(entity.category_id)),
            location_id=ID(str(entity.location_id)),
            reviewed=entity.reviewed,
        )
