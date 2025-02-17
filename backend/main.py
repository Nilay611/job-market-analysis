from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from routes import job_posting_router, company_router

app = FastAPI()
app.include_router(job_posting_router)
app.include_router(company_router)


@app.get("/")
async def root():
    return {"message": "Job Market Analytics API is running"}


@app.get("/ping-db")
async def ping_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute("SELECT 1")
        return {"status": "success", "message": "Database connected! Result - {0}".format(result)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
