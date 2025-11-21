from fastapi import FastAPI
from app.db import engine, Base
from app.routers import users_router, trips_router, documents_router

# Create database tables
# In production will use alembic
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FreightFlowAI Backend",
    description="API for logistics agentic workflows",
    version="0.1.0"
)

# include routers

app.include_router(users_router)
app.include_router(trips_router)
app.include_router(documents_router)

@app.get("/")
def read_root():
    return {"message": "FreightFlowAI backend running"}