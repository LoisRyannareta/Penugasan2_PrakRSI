from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.backend.schemas.role import RoleCreate, RoleResponse
from src.backend.services.role_service import (
    create_role_service,
    get_all_roles_service,
    get_role_by_id_service,
    delete_role_service
)
from src.backend.database.db import get_db

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RoleResponse)
def create_role(data: RoleCreate, db: Session = Depends(get_db)):
    return create_role_service(db, data)

@router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return get_all_roles_service(db)

@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    return get_role_by_id_service(db, role_id)

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    delete_role_service(db, role_id)
    return {"message": "Role deleted"}