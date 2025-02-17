from sqlalchemy import Column, BigInteger, Index
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class JobIndustry(Base):
    __tablename__ = 'job_industries'
    id = Column(BigInteger, primary_key=True, index=True)
    job_id = Column(BigInteger, index=True)
    industry_id = Column(BigInteger, index=True)


class JobIndustrySchema(BaseModel):
    id: int
    job_id: int
    industry_id: int

    class Config:
        from_attributes = True
