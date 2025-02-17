from sqlalchemy import Column, BigInteger, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class CompanySpeciality(Base):
    __tablename__ = 'company_specialities'
    id = Column(BigInteger, primary_key=True, index=True)
    company_id = Column(BigInteger, index=True)
    speciality = Column(Text, nullable=False)


class CompanySpecialitySchema(BaseModel):
    id: int
    company_id: int
    speciality: str

    class Config:
        from_attributes = True
