from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import follow_service
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/follow",
    tags=["Follow"]
)


@router.post(
    "/{user_id}",
    status_code=status.HTTP_201_CREATED
)
async def follow_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        return follow_service.follow_user(
            db,
            current_user.id,
            user_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK
)
async def unfollow_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        follow_service.unfollow_user(
            db,
            current_user.id,
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