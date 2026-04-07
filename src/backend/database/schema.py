from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# 1. Tabel Role
class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

# 2. Tabel User
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=255)
    last_name: Optional[str] = Field(default=None, max_length=255)
    whatsapp: str = Field(max_length=30)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

# 3. Tabel Account
class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    role_id: int = Field(foreign_key="role.id")
    email: str
    username: str = Field(max_length=16)
    password: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

# 4. Tabel Event
class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    quota: int # smallint di gambar
    started_at: datetime
    ended_at: datetime
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

# 5. Tabel Registration
class Registration(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    event_id: int = Field(foreign_key="event.id")

# 6. Tabel Log (Ada di gambar paling atas)
class Log(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    account_id: int = Field(foreign_key="account.id")
    created_at: datetime = Field(default_factory=datetime.now)
    action: str # ACTION (enum/text)
    ip_address: str
    user_agent: str
    entity: str
    entity_id: Optional[int] = None