from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.dependencies import get_db

from schemas.user import (
    UserRegister,
    UserResponse
)

from schemas.login import UserLogin
from services.user_services import register_user, login_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

#====================================#
#=============REGISTER===============#
#====================================#

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):

    return register_user(
        db=db,
        user_data=user_data
    )


#====================================#
#================LOGIN===============#
#====================================#  


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    return login_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )