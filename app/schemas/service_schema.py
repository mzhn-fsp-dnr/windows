from pydantic import BaseModel, UUID4
from typing import Optional, List

class ServiceBase(BaseModel):
    name: str
    parent_id: Optional[UUID4]

class ServiceSchema(ServiceBase):
    id: UUID4
    children: List["ServiceSchema"] = []

    class Config:
        from_attributes = True