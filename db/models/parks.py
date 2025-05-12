from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from db.base import Base

class Parks(Base):
    __tablename__ = 'parks'
    __table_args__ = {"schema": "mlb"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey('mlb.teams.id'), nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    opened_date = Column(DateTime, nullable=False)