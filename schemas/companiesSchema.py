from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from coreSchema import DateTimeModelMixin


class CompanyBase(BaseModel):
    name: str
    hq: Optional[str]
    symbol_id: int
    subindustry_id: Optional[str]
    m_description: Optional[str]
    exchange_id: Optional[int]


class Company(CompanyBase):
    class Config():
        orm_mode = True


class CompanyView(BaseModel):
    name: str
    symbol_id: int

    class Config():
        orm_mode = True


class ComanyDetail(CompanyBase, DateTimeModelMixin):
    name: str
    hq: str
    symbol_id: int
    subindustry_id: str
    m_description: str
    exchange_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config():
        orm_mode = True


class CompanyCreate(BaseModel):
    name: str
    symbol_id: int

    class Config():
        orm_mode = True


class CompanyUpdate(BaseModel):
    name: Optional[str]
    hq: Optional[str]
    symbol_id: Optional[int]
    subindustry_id: Optional[str]
    m_description: Optional[str]
    exchange_id: Optional[int]

    class Config():
        orm_mode = True




