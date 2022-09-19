# conda activate BaseApp
# uvicorn app.main:app --reload
# from pydoc import describe
from fastapi import FastAPI, Request
from app.routers import router

app = FastAPI(
    title="BaseApp",
    description=("BaseApp"),
    vesrion="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc"
)

app.include_router(router)