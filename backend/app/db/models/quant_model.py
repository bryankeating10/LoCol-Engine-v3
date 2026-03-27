from app.db.db import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship as rel
from datetime import datetime

class Quant(Base):
    __tablename__ = 'quants'

    # Identification
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Relationships
    testers = rel('Tester', back_populates='quant')

    # Time stamp
    created_at = Column(DateTime, default=datetime.now, nullable=False)