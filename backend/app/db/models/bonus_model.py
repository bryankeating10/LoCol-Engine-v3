from app.db.db import Base
from app.db.models.casino_model import Casino
from sqlalchemy import Column, Integer, String, DateTime

class Bonus(Base):
    __tablename__ = 'bonuses'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, default=f'{}')