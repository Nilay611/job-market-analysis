from sqlalchemy import Column, BigInteger, Index, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class JobSkill(Base):
    __tablename__ = 'job_skills'
    id = Column(BigInteger, primary_key=True, index=True)
    job_id = Column(BigInteger)
    skill_id = Column(BigInteger)


class JobSkillSchema(BaseModel):
    id: int
    job_id: int
    skill_id: int

    class Config:
        from_attributes = True
