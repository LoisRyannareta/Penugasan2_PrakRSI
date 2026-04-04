from sqlmodel import Session, select
from src.backend.database.schema import User

# CREATE
def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# GET ALL
def get_all_users(db: Session):
    return db.exec(select(User)).all()

# GET BY ID
def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)

# UPDATE
def update_user(db: Session, user_id: int, user_data):
    user = db.get(User, user_id)
    
    if not user:
        return None

    # update field satu per satu
    if user_data.name is not None:
        user.name = user_data.name
    if user_data.email is not None:
        user.email = user_data.email

    db.commit()
    db.refresh(user)
    return user

# DELETE
def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()