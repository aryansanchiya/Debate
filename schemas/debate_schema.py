from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class DebateStatus(str, Enum):
    UPCOMING = "UPCOMING"
    LIVE = "LIVE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class DebateType(str, Enum):
    CHAT = "CHAT"
    # VIDEO = "VIDEO"
    VOICE = "VOICE"


class DebateCreate(BaseModel):
    title: str
    description: str
    category: str
    debate_type: DebateType
    participants_per_side: int
    argument_time_seconds: int
    start_time: datetime
    end_time: datetime
    is_private: bool = False
    audience_limit: Optional[int] = None
    rules: Optional[str] = None


class DebateResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    debate_type: DebateType
    status: DebateStatus
    participants_per_side: int
    argument_time_seconds: int
    start_time: datetime
    end_time: datetime
    is_private: bool
    audience_limit: Optional[int]
    rules: Optional[str]
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True