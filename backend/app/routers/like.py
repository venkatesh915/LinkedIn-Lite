from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import like_service
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/likes",
    tags=["Likes"]
)


@router.post(
    "/{post_id}",
    status_code=status.HTTP_201_CREATED
)
async def like_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        return like_service.like_post(
            db,
            current_user.id,
            post_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete(
    "/{post_id}",
    status_code=status.HTTP_200_OK
)
async def unlike_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        like_service.unlike_post(
            db,
            current_user.id,
            post_id
        )

        return {
            "message": "Post unliked successfully"
        }

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get(
    "/{post_id}/count",
    status_code=status.HTTP_200_OK
)
async def get_likes_count(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        return like_service.get_post_likes(
            db,
            post_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get(
    "/{post_id}/users",
    status_code=status.HTTP_200_OK
)
async def get_liked_users(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        return like_service.get_post_likes(
            db,
            post_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )