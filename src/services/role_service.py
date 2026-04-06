from sqlmodel import Session
from fastapi import HTTPException
from src.database.schema import Role
from src.repositories.role_repository import (
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

def update_role_service(db: Session, role_id: int, data):
    role = get_role_by_id(db, role_id)

    if not role:
        raise HTTPException(404, "Role not found")

    role.name = data.name

    db.add(role)
    db.commit()
    db.refresh(role)

    return role

def patch_role_service(db: Session, role_id: int, data):
    role = get_role_by_id(db, role_id)

    if not role:
        raise HTTPException(404, "Role not found")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(role, key, value)

    db.add(role)
    db.commit()
    db.refresh(role)

    return role