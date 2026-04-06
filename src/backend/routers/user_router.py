from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.schemas.user import UserCreate, UserResponse, UserUpdate
from src.backend.services.user_service import (
    create_user_service,
    get_all_users_service,
    get_user_by_id_service,
    delete_user_service,
    update_user_service 
)
from src.backend.database.db import get_db  # pastikan ini ada

router = APIRouter(prefix="/users", tags=["Users"])

# CREATE
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)

# GET ALL
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return get_all_users_service(db)

# GET BY ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id_service(db, user_id)

# UPDATE
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user_service(db, user_id, user)

# DELETE
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    delete_user_service(db, user_id)
    return {"message": "User deleted"}