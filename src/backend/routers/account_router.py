from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.schemas.account import AccountCreate, AccountResponse
from src.backend.services.account_service import (
    create_account_service,
    get_all_accounts_service,
    get_account_by_id_service,
    delete_account_service
)
from src.backend.database.db import get_db

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account_service(db, account)

@router.get("/", response_model=list[AccountResponse])
def get_accounts(db: Session = Depends(get_db)):
    return get_all_accounts_service(db)

@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)):
    return get_account_by_id_service(db, account_id)

@router.delete("/{account_id}")
def delete_account(account_id: int, db: Session = Depends(get_db)):
    delete_account_service(db, account_id)
    return {"message": "Account deleted"}