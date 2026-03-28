from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship as rel
from app.db.db import Base
from datetime import datetime

class Account(Base):
    __tablename__ = 'accounts'

    # Identification
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)

    # Information
    tester_id = Column(Integer, ForeignKey('testers.id'))
    casino_id = Column(Integer, ForeignKey('casinos.id'))
    balance = Column(Integer, nullable=False)
    banned = Column(Boolean, nullable=False, default=False)
    suspended = Column(Boolean, nullable=False, default=False)

    # Relationships
    tester = rel('Tester', back_populates='accounts')
    casino = rel('Casino', back_populates='accounts')

    # Time stamp
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)

