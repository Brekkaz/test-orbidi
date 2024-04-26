from pydantic import BaseModel
from uuid import UUID

class Location(BaseModel):
    id: UUID
    name: str