from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class Location(BaseModel):
    id: UUID
    name: str
    latitude: float
    longitude: float


class LocationReview(BaseModel):
    """
    Representa la relacion entre una categoria y una ubicacion.\n
    Notas: los campos id y reviewed retornan null en el caso de las 
    ubicaciones que no han sido revisadas.
    """
    id: Optional[UUID]
    category_id: UUID
    location_id: UUID
    reviewed: Optional[datetime]
