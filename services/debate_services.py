from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Debate
from schemas.debate_schema import (
    DebateCreate,
    DebateStatus
)


def create_debate(db: Session, debate_data: DebateCreate, current_user_id: int):
    if (
        debate_data.end_time
        <= debate_data.start_time
    ):
        raise HTTPException(
            status_code=400,
            detail="End time must be greater than start time"
        )
    
    new_debate = Debate(
        title=debate_data.title,
        description=debate_data.description,
        category=debate_data.category,
        debate_type=debate_data.debate_type,
        status=DebateStatus.UPCOMING,
        participants_per_side=debate_data.participants_per_side,
        argument_time_seconds=debate_data.argument_time_seconds,
        start_time=debate_data.start_time,
        end_time=debate_data.end_time,
        is_private=debate_data.is_private,
        audience_limit=debate_data.audience_limit,
        rules=debate_data.rules,
        created_by=current_user_id
    )
    db.add(new_debate)
    db.commit()
    db.refresh(new_debate)
    return new_debate
    