from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import JobPosting, Skill, JobSkill
from db.database import get_db
from models.job_posting import JobPostingSchema

router = APIRouter()


@router.get("/job-postings", response_model=list[JobPostingSchema])
async def get_job_postings(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(JobPosting).limit(500))
    job_postings = result.scalars().all()
    return job_postings


@router.get("/job-postings/{job_id}", response_model=JobPostingSchema)
async def get_job_posting(job_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(JobPosting).where(JobPosting.job_id == job_id))
    job_posting = result.scalar_one_or_none()
    if not job_posting:
        raise HTTPException(status_code=404, detail="Job posting not found")
    return job_posting


@router.get("/search-job-postings/{skill_abr}", response_model=list[JobPostingSchema])
async def search_job_postings(skill_abr: str, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(JobPosting)
        .join(JobSkill, JobSkill.job_id == JobPosting.job_id)
        .join(Skill, JobSkill.skill_id == Skill.skill_id)
        .where(Skill.skill_abr.ilike(f"%{skill_abr}%"))
    )
    result = await db.execute(stmt)
    job_postings = result.scalars().all()
    return job_postings
