from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.db import Base
from sqlalchemy.orm import relationship as rel
from datetime import datetime

class Action(Base):
    __tablename__ = 'actions'

    # Identification
    id = Column(Integer, primary_key=True)

    # Information
    category = Column(String, nullable=False)
    """
    Action categories:
    - Sign-Up
    - Deposit
    - Play
    - Withdrawal
    """
    magnitude = Column(Float, nullable=True)
    account_id = Column(Integer, nullable=False)
    location_id = Column(Integer, nullable=True)
    start_balance = Column(Float, nullable=True)
    end_balance = Column(Float, nullable=True)
    wagered = Column(Float, nullable=True)

    # Relationships
    account = rel('Account', back_populates='actions')
    location = rel('Location', back_populates='actions')

    # Time stamp
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)
