from uuid import UUID

from pydantic import BaseModel

from domain.entities.location import Location 


class LocationModel(BaseModel):
    id: UUID
    name: str

    def to_entity(self) -> Location:
        return Location(
            id=self.id,
            name=self.name,
        )
