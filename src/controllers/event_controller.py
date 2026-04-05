from fastapi import Depends
from sqlmodel import Session
from src.services.event_service import EventService
from src.database.connection import get_session
from src.dto.event import EventCreate


service = EventService()


def get_events(db: Session = Depends(get_session)):
    return service.get_events(db)


def get_event(event_id: int, db: Session = Depends(get_session)):
    return service.get_event(db, event_id)


def create_event(data: EventCreate, db: Session = Depends(get_session)):
    return service.create_event(db, data)


def update_event(event_id: int, data: EventCreate, db: Session = Depends(get_session)):
    return service.update_event(db, event_id, data)


def delete_event(event_id: int, db: Session = Depends(get_session)):
    return service.delete_event(db, event_id)