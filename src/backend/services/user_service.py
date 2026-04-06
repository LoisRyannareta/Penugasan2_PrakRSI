from sqlmodel import Session
from src.backend.database.schema import User
from src.backend.repositories.user_repository import (
    create_user,
    get_user_by_id,
    get_all_users,
    delete_user, 
    update_user
)

def create_user_service(db: Session, user_data):
    user = User(**user_data.dict())
    return create_user(db, user)

def update_user_service(db: Session, user_id: int, user_data):
    user = update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_all_users_service(db: Session):
    return get_all_users(db)

def get_user_by_id_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise Exception("User not found")
    return user

def delete_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise Exception("User not found")
    delete_user(db, user)