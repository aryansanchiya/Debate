from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.dependencies import get_db

from schemas.user import (
    UserRegister,
    UserResponse,
    UserUpdate,
    DeleteResponse
)

from schemas.login import UserLogin
from services.user_services import register_user, login_user, update_user, delete_user 


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

# ====================================#
# =============UPDATE USER============# NEW
# ====================================#

@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Update User",
    description="Update user by user ID - only send fields you want to update"
)
def update(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    return update_user(
        db=db,
        user_id=user_id,
        user_data=user_data
    )


# ====================================#
# =============DELETE USER============# NEW
# ====================================#

@router.delete(
    "/{user_id}",
    response_model=DeleteResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete User",
    description="Permanently delete a user by user ID"
)
def delete(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user(
        db=db,
        user_id=user_id
    )
