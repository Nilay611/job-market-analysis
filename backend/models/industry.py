from sqlalchemy import Column, BigInteger, Text, Index
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class Industry(Base):
    __tablename__ = 'industries'
    industry_id = Column(BigInteger, primary_key=True, index=True)
    industry_name = Column(Text, nullable=False)


class IndustrySchema(BaseModel):
    industry_id: int
    industry_name: str

    class Config:
        from_attributes = True
