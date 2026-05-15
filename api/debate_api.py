from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db

from schemas.debate_schema import (
    DebateCreate,
    DebateResponse
)

from services.debate_services import create_debate

from core.current_user import get_current_user


router = APIRouter(
    prefix="/debates",
    tags=["Debates"]
)


@router.post(
    "/create",
    response_model=DebateResponse
)
def create_debate_api(
    debate_data: DebateCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return create_debate(
        db=db,
        debate_data=debate_data,
        current_user_id=current_user.id
    )