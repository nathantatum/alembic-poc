from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from db.base import Base

class Teams(Base):
    __tablename__ = 'teams'
    __table_args__ = {"schema": "mlb"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    founded_date = Column(DateTime, nullable=False)