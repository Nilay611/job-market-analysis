from sqlalchemy import Column, BigInteger, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime

Base = declarative_base()


class EmployeeCount(Base):
    __tablename__ = 'employee_counts'
    id = Column(BigInteger, primary_key=True, index=True)
    company_id = Column(BigInteger, index=True)
    employee_count = Column(BigInteger, nullable=False)
    follower_count = Column(BigInteger, nullable=False)
    time_recorded = Column(DateTime, nullable=False)


class EmployeeCountSchema(BaseModel):
    id: int
    company_id: int
    employee_count: int
    follower_count: int
    time_recorded: datetime

    class Config:
        from_attributes = True
