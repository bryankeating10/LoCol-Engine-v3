from app.db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship as rel
from datetime import datetime

class Blacklist(Base):
    __tablename__ = 'blacklists'

    # Identification
    id = Column(Integer, primary_key=True)

    # Information
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    casino_id = Column(Integer, ForeignKey('casinos.id'), nullable=False)
    probable_action_id = Column(Integer, nullable=True)
    active = Column(Boolean, nullable=False, default=True)

    # Relationships
    location = rel('Location', back_populates='blacklists')
    casino = rel('Casino', back_populates='blacklists')

    # Time stamp
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)

