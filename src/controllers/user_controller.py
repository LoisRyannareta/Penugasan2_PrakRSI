from fastapi import Depends
from sqlmodel import Session

from src.database.connection import get_session
from src.dto.user import UserCreate, UserUpdate
from src.services.user_service import (
    create_user_service,
    get_all_users_service,
    get_user_by_id_service,
    update_user_service,
    delete_user_service,
)


def get_users(db: Session = Depends(get_session)):
    return get_all_users_service(db)


def get_user(user_id: int, db: Session = Depends(get_session)):
    return get_user_by_id_service(db, user_id)


def create_user(data: UserCreate, db: Session = Depends(get_session)):
    return create_user_service(db, data)


def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_session)):
    return update_user_service(db, user_id, data)


def delete_user(user_id: int, db: Session = Depends(get_session)):
    return delete_user_service(db, user_id)