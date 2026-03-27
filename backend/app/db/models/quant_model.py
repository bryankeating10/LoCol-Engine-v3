from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship as rel

class Quant(Base):
    __tablename__ = 'quant'

    # Identification
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Relationships
    testers = rel('Tester', back_populates='quant')