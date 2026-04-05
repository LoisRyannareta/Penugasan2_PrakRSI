from datetime import datetime
from fastapi import HTTPException
from sqlmodel import Session
from src.database.schema.schema import Account, User, Role
from src.repositories.account_repository import (
    create_account,
    get_account_by_id,
    get_all_accounts,
    delete_account
)

def create_account_service(db: Session, account_data):
    user = db.get(User, account_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    role = db.get(Role, account_data.role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    now = datetime.now()
    account = Account(
        **account_data.dict(),
        created_at=now,
        updated_at=now,
    )
    return create_account(db, account)

def get_all_accounts_service(db: Session):
    return get_all_accounts(db)

def get_account_by_id_service(db: Session, account_id: int):
    account = get_account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

def delete_account_service(db: Session, account_id: int):
    account = get_account_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    delete_account(db, account)