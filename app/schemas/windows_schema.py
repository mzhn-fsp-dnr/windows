from typing import List
from pydantic import BaseModel
from . import service_schema

class WindowBase(BaseModel):
    name: str
    services: List[service_schema.ServiceSchema] = []
    
class Window(WindowBase):
    id: int

    class Config:
        from_attributes = True