from datetime import datetime
from pydantic import field_validator, ValidationInfo, BaseModel


class EventCreate(BaseModel):
    name: str
    description: str
    quota: int
    started_at: datetime
    ended_at: datetime

    @field_validator("quota")
    def validate_quota(cls, v):
        if v <= 0:
            raise ValueError("Quota harus lebih dari 0")
        return v

    @field_validator("ended_at")
    def validate_time(cls, v, info: ValidationInfo):
        started_at = info.data.get("started_at")
        if started_at and v <= started_at:
            raise ValueError("ended_at harus lebih besar dari started_at")
        return v


class EventResponse(BaseModel):
    id: int
    name: str
    description: str
    quota: int
    started_at: datetime
    ended_at: datetime

    class Config:
        from_attributes = True