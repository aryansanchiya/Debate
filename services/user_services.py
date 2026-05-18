from fastapi import HTTPException
# from db.database import
from models import User
from sqlalchemy.orm import Session
from schemas.user import UserRegister, UserUpdate
from core.security import hash_password, create_access_token, verify_password

def register_user(db:Session, user_data:UserRegister):
    existing_email = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(      ###HASH PASSWORD WE USED FROM core/security.py
            user_data.password
        ),
        interest=user_data.interest,
        birth_date=user_data.birth_date,
        preference=user_data.preference,
        bio=user_data.bio
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "user_id": user.id,
            "email": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }

def update_user(db: Session, user_id: int, user_data: UserUpdate):

    
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User with ID {user_id} not found"
        )

    
    update_data = user_data.model_dump(exclude_unset=True)

    
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No fields provided to update"
        )

    
    if "email" in update_data:
        existing_email = db.query(User).filter(
            User.email == update_data["email"],
            User.id != user_id
        ).first()

        if existing_email:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    
    if "username" in update_data:
        existing_username = db.query(User).filter(
            User.username == update_data["username"],
            User.id != user_id
        ).first()

        if existing_username:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

    
    if "password" in update_data:
        update_data["hashed_password"] = hash_password(
            update_data.pop("password")
        )

    
    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):

    # User find karo
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User with ID {user_id} not found"
        )

    user_info = {
        "message": "User deleted successfully",
        "user_id": user.id,
        "username": user.username
    }

    db.delete(user)
    db.commit()

    return user_info