from sqlalchemy import Column, BigInteger, Text, Index
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class Skill(Base):
    __tablename__ = 'skills'
    skill_id = Column(BigInteger, primary_key=True, index=True)
    skill_abr = Column(Text, nullable=False)
    skill_name = Column(Text, nullable=False)


class SkillSchema(BaseModel):
    skill_id: int
    skill_abr: str
    skill_name: str

    class Config:
        from_attributes = True
