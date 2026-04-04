from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.schemas.registration import RegistrationCreate, RegistrationResponse
from src.backend.services.registration_service import (
    create_registration_service,
    get_all_registrations_service,
    get_registration_by_id_service,
    delete_registration_service
)
from src.backend.database.db import get_db

router = APIRouter(prefix="/registrations", tags=["Registrations"])

# CREATE
@router.post("/", response_model=RegistrationResponse)
def create_registration(data: RegistrationCreate, db: Session = Depends(get_db)):
    return create_registration_service(db, data)

# GET ALL
@router.get("/", response_model=list[RegistrationResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_registrations_service(db)

# GET BY ID
@router.get("/{registration_id}", response_model=RegistrationResponse)
def get_by_id(registration_id: int, db: Session = Depends(get_db)):
    return get_registration_by_id_service(db, registration_id)

# DELETE
@router.delete("/{registration_id}")
def delete(registration_id: int, db: Session = Depends(get_db)):
    delete_registration_service(db, registration_id)
    return {"message": "Registration deleted"}