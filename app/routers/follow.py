from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import follow_service

router = APIRouter(
    prefix="/follow",
    tags=["Follow"]
)


# --------------------------------
# Follow a User
# --------------------------------
@router.post(
    "/{user_id}",
    status_code=status.HTTP_201_CREATED
)
async def follow_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        return follow_service.follow_user(
            db,
            user_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# --------------------------------
# Unfollow a User
# --------------------------------
@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK
)
async def unfollow_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        follow_service.unfollow_user(
            db,
            user_id
        )

        return {
            "message": "User unfollowed successfully"
        }

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# --------------------------------
# Get Followers
# --------------------------------
@router.get(
    "/followers/{user_id}",
    status_code=status.HTTP_200_OK
)
async def get_followers(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        return follow_service.get_followers(
            db,
            user_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# --------------------------------
# Get Following
# --------------------------------
@router.get(
    "/following/{user_id}",
    status_code=status.HTTP_200_OK
)
async def get_following(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        return follow_service.get_following(
            db,
            user_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )