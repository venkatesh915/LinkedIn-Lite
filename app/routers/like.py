from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import like_service

router = APIRouter(
    prefix="/likes",
    tags=["Likes"]
)


# --------------------------------
# Like a Post
# --------------------------------
@router.post(
    "/{post_id}",
    status_code=status.HTTP_201_CREATED
)
async def like_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        return like_service.like_post(
            db,
            post_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# --------------------------------
# Unlike a Post
# --------------------------------
@router.delete(
    "/{post_id}",
    status_code=status.HTTP_200_OK
)
async def unlike_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        like_service.unlike_post(
            db,
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


# --------------------------------
# Get Likes Count
# --------------------------------
@router.get(
    "/{post_id}/count",
    status_code=status.HTTP_200_OK
)
async def get_likes_count(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        return like_service.get_likes_count(
            db,
            post_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# --------------------------------
# Get Users Who Liked a Post
# --------------------------------
@router.get(
    "/{post_id}/users",
    status_code=status.HTTP_200_OK
)
async def get_liked_users(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        return like_service.get_liked_users(
            db,
            post_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )