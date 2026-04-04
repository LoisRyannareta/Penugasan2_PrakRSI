from fastapi import FastAPI
from src.backend.database.db import Base, engine
from src.backend.routers import user_router, account_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Backend RSI API",
    version="1.0.0"
)

# Root (biar tahu API hidup)
@app.get("/")
def root():
    return {"message": "API is running 🚀"}

# Register router
app.include_router(user_router.router)
app.include_router(account_router.router)