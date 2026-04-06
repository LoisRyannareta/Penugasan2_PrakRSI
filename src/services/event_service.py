from sqlmodel import Session, select
from src.repositories.event_repository import EventRepository
from src.database.schema import Event
from datetime import datetime
from fastapi import HTTPException


class EventService:

    def __init__(self):
        self.repo = EventRepository()

    def get_events(self, db: Session):
        return self.repo.get_all(db)

    def get_event(self, db: Session, event_id: int):
        return self.repo.get_by_id(db, event_id)

    def create_event(self, db: Session, data):
        event = Event(
            **data.dict(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return self.repo.create(db, event)

    def update_event(self, db: Session, event_id: int, data):
        event = self.repo.get_by_id(db, event_id)

        if not event:
            raise HTTPException(404, "Event not found")

        event.name = data.name
        event.description = data.description
        event.quota = data.quota
        event.started_at = data.started_at
        event.ended_at = data.ended_at
        event.updated_at = datetime.now()

        return self.repo.update(db, event)

    def delete_event(self, db: Session, event_id: int):
        event = self.repo.get_by_id(db, event_id)

        if not event:
            raise HTTPException(404, "Event not found")

        self.repo.delete(db, event)
        return event

  
    def patch_event(self, db: Session, event_id: int, data):
        event = self.repo.get_by_id(db, event_id)

        if not event:
            raise HTTPException(404, "Event not found")

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(event, key, value)

        event.updated_at = datetime.now()

        return self.repo.update(db, event)


    def search_events(self, db: Session, name=None, location=None):
        statement = select(Event)

        if name:
            statement = statement.where(Event.name.contains(name))

        if location:
            statement = statement.where(Event.location.contains(location))

        return db.exec(statement).all()