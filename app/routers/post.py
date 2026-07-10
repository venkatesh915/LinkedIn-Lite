from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.post import (
    PostCreate,
    PostResponse
)

from app.services import post_service

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# -----------------------------
# Create Post
# -----------------------------
@router.post(
    "/",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_post(
    post: PostCreate,
    db: Session = Depends(get_db)
):
    try:
        return post_service.add_post(db, post)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# -----------------------------
# Get All Posts
# -----------------------------
@router.get(
    "/",
    status_code=status.HTTP_200_OK
)
async def get_posts(
    db: Session = Depends(get_db)
):
    try:
        return post_service.list_posts(db)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# -----------------------------
# Get Single Post
# -----------------------------
@router.get(
    "/{post_id}",
    response_model=PostResponse
)
async def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        return post_service.get_post(
            db,
            post_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# -----------------------------
# Update Post
# -----------------------------
@router.put(
    "/{post_id}",
    response_model=PostResponse
)
async def update_post(
    post_id: int,
    post: PostCreate,
    db: Session = Depends(get_db)
):
    try:
        return post_service.edit_post(
            db,
            post_id,
            post
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# -----------------------------
# Delete Post
# -----------------------------
@router.delete(
    "/{post_id}",
    status_code=status.HTTP_200_OK
)
async def delete_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        post_service.remove_post(
            db,
            post_id
        )

        return {
            "message": "Post deleted successfully"
        }

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )