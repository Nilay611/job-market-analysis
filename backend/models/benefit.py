from sqlalchemy import Column, BigInteger, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class Benefit(Base):
    __tablename__ = 'benefits'
    id = Column(BigInteger, primary_key=True, index=True)
    job_id = Column(BigInteger, index=True)
    inferred = Column(Boolean, nullable=False)
    benefit_type = Column(Text, nullable=False)


class BenefitSchema(BaseModel):
    id: int
    job_id: int
    inferred: bool
    benefit_type: str

    class Config:
        from_attributes = True
