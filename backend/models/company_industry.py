from sqlalchemy import Column, BigInteger, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class CompanyIndustry(Base):
    __tablename__ = 'company_industries'
    id = Column(BigInteger, primary_key=True, index=True)
    company_id = Column(BigInteger, index=True)
    industry_id = Column(BigInteger, index=True)


class CompanyIndustrySchema(BaseModel):
    id: int
    company_id: int
    industry_id: int

    class Config:
        from_attributes = True
