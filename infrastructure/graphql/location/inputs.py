import strawberry

from pydantic import BaseModel, Field
from domain.entities.location import Location, LocationReview
from uuid import UUID
from datetime import datetime


class LocationObject(BaseModel):
    """
    Valida y parsea la entrada de ubicaciones
    """
    name: str = Field(min_length=3, max_length=100)
    latitude: float = Field(gt=0, lt=999999)
    longitude: float = Field(gt=0, lt=999999)

    def to_entity(self, id: UUID):
        return Location(
            id=id, name=self.name, latitude=self.latitude, longitude=self.longitude
        )


@strawberry.experimental.pydantic.input(model=LocationObject, all_fields=True)
class LocationInput:
    pass


class ReviewObject(BaseModel):
    """
    Valida y parsea la entrada de revisiones
    """
    category_id: UUID = Field()
    location_id: UUID = Field()

    def to_entity(self, id: UUID):
        return LocationReview(
            id=id,
            category_id=self.category_id,
            location_id=self.location_id,
            reviewed=datetime.now(),
        )


@strawberry.experimental.pydantic.input(model=ReviewObject, all_fields=True)
class ReviewInput:
    pass
