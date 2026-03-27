from app.db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship as rel
from datetime import datetime

class Bonus(Base):
    __tablename__ = 'bonuses'

    # Identification
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Information
    casino_id = Column(Integer, ForeignKey('casinos.id'))
    bonus_type = Column(String, nullable=False)
    bonus_value = Column(Integer, nullable=False)
    location_sensitive = Column(Boolean, nullable=False)

    # Relationships
    casino = rel('Casino', back_populates='bonuses')

    # Time stamp
    discovery = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)