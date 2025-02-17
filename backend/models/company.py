from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    company_state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    city = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)
    address = Column(Text, nullable=True)
    url = Column(Text, nullable=True)


class CompanySchema(BaseModel):
    company_id: int
    company_name: Optional[str]
    description: Optional[str]
    company_state: Optional[str]
    country: Optional[str]
    city: Optional[str]
    zip_code: Optional[str]
    address: Optional[str]
    url: Optional[str]

    class Config:
        from_attributes = True
