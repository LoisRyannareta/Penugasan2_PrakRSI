from fastapi import HTTPException
from sqlmodel import Session, select
from src.database.schema.schema import User
from datetime import datetime
from src.repositories.user_repository import (
    create_user,
    get_user_by_id,
    get_all_users,
    delete_user,
    update_user
)

def create_user_service(db: Session, user_data):
    now = datetime.now()
    user = User(
        **user_data.dict(),
        created_at=now,
        updated_at=now,
    )
    return create_user(db, user)

def update_user_service(db: Session, user_id: int, user_data):
    user = update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.updated_at = datetime.now()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users_service(db: Session):
    return get_all_users(db)

def get_user_by_id_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, user)

def search_users_service(db: Session, name: str = None, email: str = None):
    query = select(User)

    if name:
        query = query.where(User.name.contains(name))

    if email:
        query = query.where(User.email.contains(email))

    return db.exec(query).all()

def patch_user_service(db: Session, user_id: int, data):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(404, "User not found")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user