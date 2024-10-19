from sqlalchemy import Column, DateTime, String, UUID, ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship
import uuid
import datetime

class Window(Base):
    __tablename__ = "windows"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    services = relationship("WindowService", back_populates="window")
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
    
class WindowService(Base):
    __tablename__ = "window_services"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    window_id = Column(UUID(as_uuid=True), ForeignKey('windows.id'))
    service_id = Column(UUID(as_uuid=True), nullable=False)
    
    window = relationship("Window", back_populates="services")