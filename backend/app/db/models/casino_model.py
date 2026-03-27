from app.db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship as rel
from datetime import datetime

class  Casino(Base):
    __tablename__ = 'casinos'

    # Identification
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Information
    network = Column(String, nullable=False)
    active = Column(Boolean, nullable=False)

    # Restriction profile
    signup_rest = Column(Boolean, nullable=False)
    deposit_rest = Column(Boolean, nullable=False)
    play_rest = Column(Boolean, nullable=False)
    withdrawal_rest = Column(Boolean, nullable=False)
    network_rest = Column(Boolean, nullable=False)

    # Relationships
    bonuses = rel('Bonus', back_populates='casino')
    accounts = rel('Account', back_populates='casino')
    actions = rel('Action', back_populates='casino')

    # Time stamp
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)
