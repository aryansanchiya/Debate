from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey
from db.database import Base
import enum
from sqlalchemy import Enum
from sqlalchemy.sql import func

class Preference(enum.Enum):
    ORGANIZER = "ORGANIZER"
    PARTICIPANT = "PARTICIPANT"
    AUDIENCE = "AUDIENCE"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30),unique=True,nullable=False)
    email = Column(String,unique=True,nullable=False, index=True)
    hashed_password = Column(String,nullable=False)
    interest = Column(String, nullable=True)
    birth_date = Column(Date, nullable=False)
    preference = Column(Enum(Preference), nullable=False)
    bio = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_banned = Column(Boolean, default=False)
    reputation_points = Column(Integer, default=0)
    total_debates = Column(Integer, default=0)
    won_debates = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

class DebateType(enum.Enum):
    CHAT = "CHAT"
    VOICE = "VOICE"

class DebateStatus(enum.Enum):
    UPCOMING = "UPCOMING"
    LIVE = "LIVE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class Debate(Base):
    __tablename__ = "debates"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    debate_type = Column(Enum(DebateType), nullable=True)
    is_private = Column(Boolean, default=False)
    rules = Column(String, nullable=True)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    status = Column(Enum(DebateStatus), default=DebateStatus.UPCOMING)
    participants_per_side = Column(Integer, nullable=False)
    audience_limit = Column(Integer, default=0)
    argument_time_seconds = Column(Integer, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


# class Teams(Base):
#     __tablename__ = "Teams"

#     id = Column(Integer, primary_key=True, index=True)
#     team_name = Column(String, nullable=False)
#     debate_id = Column(Integer, ForeignKey("Debate.id"), nullable=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     win_count = Column(Integer, default=0)
