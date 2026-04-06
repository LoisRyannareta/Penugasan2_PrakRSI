from sqlmodel import Session, select
from fastapi import HTTPException
from src.database.schema import Registration, User, Event
from src.repositories.registration_repository import (
    create_registration,
    get_all_registrations,
    get_registration_by_id,
    get_registration_by_id
)


def create_registration_service(db: Session, data):

    user = db.get(User, data.user_id)
    if not user:
        raise HTTPException(404, "User not found")

    event = db.get(Event, data.event_id)
    if not event:
        raise HTTPException(404, "Event not found")

    existing = db.exec(
        select(Registration)
        .where(Registration.user_id == data.user_id)
        .where(Registration.event_id == data.event_id)
    ).first()

    if existing:
        raise HTTPException(400, "User already registered for this event")

    registration = Registration(**data.model_dump())
    return create_registration(db, registration)


def get_all_registrations_service(db: Session):
    return get_all_registrations(db)


def get_registration_by_id_service(db: Session, registration_id: int):
    reg = get_registration_by_id(db, registration_id)
    if not reg:
        raise HTTPException(404, "Registration not found")
    return reg

def delete_registration_service(db: Session, registration_id: int):
    reg = get_registration_by_id(db, registration_id)
    if not reg:
        raise HTTPException(404, "Registration not found")
    delete_registration(db, reg)

def search_registrations_service(
    db: Session,
    user_id: int = None,
    event_id: int = None
):
    query = select(Registration)

    if user_id:
        query = query.where(Registration.user_id == user_id)

    if event_id:
        query = query.where(Registration.event_id == event_id)

    return db.exec(query).all()

def patch_registration_service(db, registration_id, data):
    registration = get_registration_by_id(db, registration_id)

    if not registration:
        raise HTTPException(404, "Registration not found")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        if hasattr(registration, key):  # 🔥 biar gak error
            setattr(registration, key, value)

    db.add(registration)
    db.commit()
    db.refresh(registration)

    return registration