from app.db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.orm import relationship as rel
from datetime import datetime

class Location(Base):
    __tablename__ = 'locations'

    # Identification
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    state = Column(String, nullable=False)

    # Information
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Relationships
    blacklists = rel('Blacklist', back_populates='location')
    actions = rel('Action', back_populates='location')

    # Time stamp
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)