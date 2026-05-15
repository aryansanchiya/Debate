from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime
from enum import Enum


class Preference(str, Enum):
    ORGANIZER = "ORGANIZER"
    PARTICIPANT = "PARTICIPANT"
    AUDIENCE = "AUDIENCE"


class UserRegister(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=30
    )

    email: EmailStr

    password: str = Field(
        min_length=6
    )

    interest: Optional[str] = None

    birth_date: date

    preference: Preference

    bio: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    interest: Optional[str]
    birth_date: date
    preference: Preference
    bio: Optional[str]

    is_active: bool
    is_banned: bool

    reputation_points: int
    total_debates: int
    won_debates: int

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True