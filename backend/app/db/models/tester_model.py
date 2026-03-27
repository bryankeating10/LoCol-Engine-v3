from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship as rel
from app.db.db import Base
from datetime import datetime, date

class Tester(Base):
    __tablename__ = 'testers'

    # Identification
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Information
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    state = Column(String, nullable=False)
    address = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    assigned_quant = Column(Integer, ForeignKey('quants.id'))

    # Relationships
    quant = rel('Quant', back_populates='testers')
    accounts = rel('Account', back_populates='tester')

    # Time stamp
    created_at = Column(DateTime, default=datetime.now, nullable=False)