from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func, case, desc, nullslast
from models import Salary, JobPosting
from db.database import get_db

router = APIRouter()


def get_yearly_salary():
    yearly_min_salary = case(
        (Salary.pay_period == 'HOURLY', Salary.min_salary * 40 * 52),
        (Salary.pay_period == 'WEEKLY', Salary.min_salary * 52),
        (Salary.pay_period == 'BIWEEKLY', Salary.min_salary * 26),
        (Salary.pay_period == 'MONTHLY', Salary.min_salary * 12),
        (Salary.pay_period == 'YEARLY', Salary.min_salary)
    )

    yearly_max_salary = case(
        (Salary.pay_period == 'HOURLY', Salary.max_salary * 40 * 52),
        (Salary.pay_period == 'WEEKLY', Salary.max_salary * 52),
        (Salary.pay_period == 'BIWEEKLY', Salary.max_salary * 26),
        (Salary.pay_period == 'MONTHLY', Salary.max_salary * 12),
        (Salary.pay_period == 'YEARLY', Salary.max_salary)
    )

    return yearly_min_salary, yearly_max_salary


async def get_salary_insights(group_by_field, db: AsyncSession, experience_level: str = None):
    yearly_min_salary, yearly_max_salary = get_yearly_salary()
    median_salary = (yearly_min_salary + yearly_max_salary) / 2

    query = (
        select(
            getattr(JobPosting, group_by_field),
            Salary.currency,
            JobPosting.listed_time,
            func.min(yearly_min_salary).label("min_salary"),
            func.avg(median_salary).label("avg_salary"),
            func.max(yearly_max_salary).label("max_salary"),
            func.percentile_cont(0.25).within_group(
                median_salary).label("percentile_25"),
            func.percentile_cont(0.50).within_group(
                median_salary).label("median_salary"),
            func.percentile_cont(0.75).within_group(
                median_salary).label("percentile_75"),
        )
        .join(JobPosting, Salary.job_id == JobPosting.job_id)
    )

    # If experience level is provided, filter the results
    if experience_level:
        query = query.filter(
            JobPosting.formatted_experience_level == experience_level)

    query = query.group_by(
        getattr(JobPosting, group_by_field), Salary.currency, JobPosting.listed_time)
    query = query.order_by(
        nullslast(desc(func.percentile_cont(0.50).within_group(median_salary))))

    result = await db.execute(query)
    salary_data = result.fetchall()

    insights = [
        {
            group_by_field: row[0],
            "currency": row.currency,
            "min_salary": row.min_salary,
            "avg_salary": row.avg_salary,
            "max_salary": row.max_salary,
            "percentile_25": row.percentile_25,
            "median_salary": row.median_salary,
            "percentile_75": row.percentile_75,
            "job_listed_time": row.listed_time
        }
        for row in salary_data
    ]

    return insights


@router.get("/salary-insights/currency/{experience_level}")
async def salary_insights_by_currency(db: AsyncSession = Depends(get_db), experience_level: str = None):
    return await get_salary_insights("currency", db, experience_level)


@router.get("/salary-insights/job-title/{experience_level}")
async def salary_insights_by_job_title(db: AsyncSession = Depends(get_db), experience_level: str = None):
    return await get_salary_insights("job_title", db, experience_level)


@router.get("/salary-insights/job-location/{experience_level}")
async def salary_insights_by_job_location(db: AsyncSession = Depends(get_db), experience_level: str = None):
    return await get_salary_insights("job_location", db, experience_level)


@router.get("/salary-insights/job-title-location/{experience_level}")
async def salary_insights_by_job_title_location(db: AsyncSession = Depends(get_db), experience_level: str = None):
    yearly_min_salary, yearly_max_salary = get_yearly_salary()
    median_salary = (yearly_min_salary + yearly_max_salary) / 2

    query = (
        select(
            JobPosting.job_title,
            JobPosting.job_location,
            Salary.currency,
            JobPosting.listed_time,
            func.min(yearly_min_salary).label("min_salary"),
            func.avg(median_salary).label("avg_salary"),
            func.max(yearly_max_salary).label("max_salary"),
            func.percentile_cont(0.25).within_group(
                median_salary).label("percentile_25"),
            func.percentile_cont(0.50).within_group(
                median_salary).label("median_salary"),
            func.percentile_cont(0.75).within_group(
                median_salary).label("percentile_75"),
        )
        .join(JobPosting, Salary.job_id == JobPosting.job_id)
    )

    # If experience level is provided, filter the results
    if experience_level:
        query = query.filter(
            JobPosting.formatted_experience_level == experience_level)

    query = query.group_by(JobPosting.job_title,
                           JobPosting.job_location, Salary.currency, JobPosting.listed_time)
    query = query.order_by(
        nullslast(desc(func.percentile_cont(0.50).within_group(median_salary))))

    result = await db.execute(query)
    salary_data = result.fetchall()

    insights = [
        {
            "job_title": row.job_title,
            "job_location": row.job_location,
            "currency": row.currency,
            "min_salary": row.min_salary,
            "avg_salary": row.avg_salary,
            "max_salary": row.max_salary,
            "percentile_25": row.percentile_25,
            "median_salary": row.median_salary,
            "percentile_75": row.percentile_75,
            "job_listed_time": row.listed_time
        }
        for row in salary_data
    ]

    return insights
