from sqlalchemy import Column, BigInteger, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional


Base = declarative_base()


class Salary(Base):
    __tablename__ = 'salaries'
    salary_id = Column(BigInteger, primary_key=True, index=True)
    job_id = Column(BigInteger)
    max_salary = Column(Float)
    med_salary = Column(Float)
    min_salary = Column(Float)
    pay_period = Column(Text)
    currency = Column(Text)
    compensation_type = Column(Text)


class SalarySchema(BaseModel):
    salary_id: int
    job_id: int
    max_salary: Optional[float]
    med_salary: Optional[float]
    min_salary: Optional[float]
    pay_period: str
    currency: str
    compensation_type: Optional[str]

    class Config:
        from_attributes = True
