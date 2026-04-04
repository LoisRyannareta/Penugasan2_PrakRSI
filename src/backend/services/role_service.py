from sqlmodel import Session
from fastapi import HTTPException
from src.backend.database.schema import Role
from src.backend.repositories.role_repository import (
    create_role,
    get_all_roles,
    get_role_by_id,
    delete_role
)

def create_role_service(db: Session, data):
    role = Role(**data.model_dump())
    return create_role(db, role)

def get_all_roles_service(db: Session):
    return get_all_roles(db)

def get_role_by_id_service(db: Session, role_id: int):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(404, "Role not found")
    return role

def delete_role_service(db: Session, role_id: int):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(404, "Role not found")
    delete_role(db, role)