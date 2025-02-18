from sqlalchemy import Column, Integer, Float, Text, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

Base = declarative_base()


class JobPosting(Base):
    __tablename__ = 'postings'
    job_id = Column(BigInteger, primary_key=True, index=True)
    company_name = Column(Text)
    job_title = Column(Text)
    description = Column(Text)
    max_salary = Column(Float)
    pay_period = Column(Text)
    job_location = Column(Text)
    company_id = Column(BigInteger)
    job_views = Column(Integer)
    med_salary = Column(Float)
    min_salary = Column(Float)
    formatted_work_type = Column(Text)
    applies = Column(Integer)
    original_listed_time = Column(DateTime)
    remote_allowed = Column(Integer)
    job_posting_url = Column(Text)
    application_url = Column(Text)
    application_type = Column(Text)
    expiry = Column(DateTime)
    closed_time = Column(DateTime)
    formatted_experience_level = Column(Text)
    skills_desc = Column(Text)
    listed_time = Column(DateTime, index=True)
    posting_domain = Column(Text)
    sponsored = Column(Integer)
    work_type = Column(Text)
    currency = Column(Text)
    compensation_type = Column(Text)
    normalized_salary = Column(Float)
    zip_code = Column(Text)
    fips = Column(Integer)


class JobPostingSchema(BaseModel):
    job_id: int
    company_name: Optional[str]
    job_title: Optional[str]
    description: Optional[str]
    max_salary: Optional[float]
    pay_period: Optional[str]
    job_location: Optional[str]
    company_id: Optional[int]
    job_views: Optional[int]
    med_salary: Optional[float]
    min_salary: Optional[float]
    formatted_work_type: Optional[str]
    applies: Optional[int]
    original_listed_time: Optional[datetime]
    remote_allowed: Optional[int]
    job_posting_url: Optional[str]
    application_url: Optional[str]
    application_type: Optional[str]
    expiry: Optional[datetime]
    closed_time: Optional[datetime]
    formatted_experience_level: Optional[str]
    skills_desc: Optional[str]
    listed_time: Optional[datetime]
    posting_domain: Optional[str]
    sponsored: Optional[int]
    work_type: Optional[str]
    currency: Optional[str]
    compensation_type: Optional[str]
    normalized_salary: Optional[float]
    zip_code: Optional[str]
    fips: Optional[int]

    class Config:
        from_attributes = True
