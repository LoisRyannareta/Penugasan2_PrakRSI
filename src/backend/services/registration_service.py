from sqlmodel import Session, select
from fastapi import HTTPException
from src.backend.database.schema import Registration, User, Event
from src.backend.repositories.registration_repository import (
    create_registration,
    get_all_registrations,
    get_registration_by_id,
    delete_registration
)

# CREATE
def create_registration_service(db: Session, data):

    # ✅ VALIDASI USER
    user = db.get(User, data.user_id)
    if not user:
        raise HTTPException(404, "User not found")

    # ✅ VALIDASI EVENT
    event = db.get(Event, data.event_id)
    if not event:
        raise HTTPException(404, "Event not found")

    # ✅ CEK DUPLIKAT
    existing = db.exec(
        select(Registration)
        .where(Registration.user_id == data.user_id)
        .where(Registration.event_id == data.event_id)
    ).first()

    if existing:
        raise HTTPException(400, "User already registered for this event")

    # ✅ SIMPAN
    registration = Registration(**data.model_dump())
    return create_registration(db, registration)


# GET ALL
def get_all_registrations_service(db: Session):
    return get_all_registrations(db)


# GET BY ID
def get_registration_by_id_service(db: Session, registration_id: int):
    reg = get_registration_by_id(db, registration_id)
    if not reg:
        raise HTTPException(404, "Registration not found")
    return reg


# DELETE
def delete_registration_service(db: Session, registration_id: int):
    reg = get_registration_by_id(db, registration_id)
    if not reg:
        raise HTTPException(404, "Registration not found")
    delete_registration(db, reg)