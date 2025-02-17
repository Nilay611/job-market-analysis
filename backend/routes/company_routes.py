from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from sqlalchemy import select, func
# Adjust these imports according to your project structure
from models import Company, JobPosting

router = APIRouter()


@router.get("/top-companies")
async def get_top_companies(db: AsyncSession = Depends(get_db)):
    stmt = (
        select(Company, func.count(JobPosting.job_id).label("job_count"))
        .join(JobPosting, JobPosting.company_id == Company.company_id)
        .group_by(Company.company_id)
        .order_by(func.count(JobPosting.job_id).desc())
    )
    result = await db.execute(stmt)
    top_companies = result.all()
    return [{"company": row.Company, "job_count": row.job_count} for row in top_companies]
