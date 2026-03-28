from app.db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship as rel
from datetime import datetime

class Bonus(Base):
    __tablename__ = 'bonuses'

    # Identification
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False) # Ex. FanDuel $1000 Deposit Lossback

    # Information
    account_id = Column(Integer, ForeignKey('accounts.id'))
    category = Column(String, nullable=False)
    """
    Bonus categories:
    - Sign-Up
    - Reload
    - VIP
    - Other
    """
    type = Column(String, nullable=False)
    """
    Bonus types:
    - Match
    - Loss Back
    - Bet Back
    - Other
    """
    rollover_multiplier = Column(Integer, nullable=True)
    volatility_rtp = Column(Float, nullable=True)
    rollover_rtp = Column(Float, nullable=True)
    expected_value = Column(Integer, nullable=True)
    location_sensitive = Column(Boolean, nullable=False, default=False)

    # Relationships
    account = rel('Account', back_populates='bonuses')

    # Time stamp
    discovery = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)