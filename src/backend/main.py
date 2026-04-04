from fastapi import FastAPI
from src.backend.database.db import init_db
from src.backend.routers import user_router, account_router

app = FastAPI(title="Acara RSI API")

# Init DB tables
init_db()

# Root (biar tahu API hidup)
@app.get("/")
def root():
    return {"message": "API is running 🚀"}

# Register router
app.include_router(user_router.router)
app.include_router(account_router.router)