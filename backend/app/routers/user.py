from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from app.schemas.auth import (
    LoginRequest,
    Token
)
from app.dependencies.auth import get_current_user
from app.services import user_service
from app.services import auth_service

router = APIRouter(
    tags=["Users"]
)


# ----------------------------
# Register User
# ----------------------------
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        new_user = user_service.create_user(db, user)
        return new_user

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# ----------------------------
# Login User
# ----------------------------
@router.post(
    "/login",
    response_model=Token
)
async def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    try:
        return auth_service.login_user(
            db,
            credentials.email,
            credentials.password
        )

    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )


# ----------------------------
# Get All Users
# ----------------------------
@router.get(
    "/users",
    response_model=list[UserResponse],
    status_code=status.HTTP_200_OK
)
async def get_all_users(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        users = user_service.get_all_users(db)
        return users

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ----------------------------
# Get User By ID
# ----------------------------
@router.get(
    "/users/{user_id}",
    response_model=UserResponse
)
async def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        user = user_service.get_user_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ----------------------------
# Update User
# ----------------------------
@router.put(
    "/users/{user_id}",
    response_model=UserResponse
)
async def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        updated_user = user_service.update_user(
            db,
            user_id,
            user
        )

        if not updated_user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return updated_user

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ----------------------------
# Delete User
# ----------------------------
@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK
)
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        deleted = user_service.delete_user(
            db,
            user_id
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return {
            "message": "User deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )