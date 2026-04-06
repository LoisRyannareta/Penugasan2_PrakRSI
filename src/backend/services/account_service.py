from sqlmodel import Session
from src.backend.database.schema import Account
from src.backend.repositories.account_repository import (
    create_account,
    get_account_by_id,
    get_all_accounts,
    delete_account
)

def create_account_service(db: Session, account_data):
    account = Account(**account_data.dict())
    return create_account(db, account)

def get_all_accounts_service(db: Session):
    return get_all_accounts(db)

def get_account_by_id_service(db: Session, account_id: int):
    account = get_account_by_id(db, account_id)
    if not account:
        raise Exception("Account not found")
    return account

def delete_account_service(db: Session, account_id: int):
    account = get_account_by_id(db, account_id)
    if not account:
        raise Exception("Account not found")
    delete_account(db, account)