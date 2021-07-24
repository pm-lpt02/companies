from sqlalchemy import Column, Integer, String, DateTime
from databases import Base
from datetime import datetime


class Company(Base):
    __tablename__ = 'companies'

    Id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    hq = Column(String, nullable=True)
    symbol_id = Column(Integer, nullable=False, index=True)
    subindustry_id = Column(Integer, nullable=True)
    m_description = Column(String, nullable=True)
    exchange_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
