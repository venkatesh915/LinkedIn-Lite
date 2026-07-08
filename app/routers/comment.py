from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import comment_service
from app.schemas.comment import (
    CommentCreate,
    CommentUpdate,
    CommentResponse
)

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


# -----------------------------
# Create Comment
# -----------------------------
@router.post(
    "/",
    response_model=CommentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_comment(
    comment: CommentCreate,
    db: Session = Depends(get_db)
):
    try:
        return comment_service.add_comment(db, comment)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# -----------------------------
# Get Comments By Post
# -----------------------------
@router.get(
    "/post/{post_id}",
    response_model=list[CommentResponse]
)
async def get_comments(
    post_id: int,
    db: Session = Depends(get_db)
):
    try:
        return comment_service.get_comments_by_post(
            db,
            post_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# -----------------------------
# Get Single Comment
# -----------------------------
@router.get(
    "/{comment_id}",
    response_model=CommentResponse
)
async def get_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):
    try:
        return comment_service.get_comment(
            db,
            comment_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# -----------------------------
# Update Comment
# -----------------------------
@router.put(
    "/{comment_id}",
    response_model=CommentResponse
)
async def update_comment(
    comment_id: int,
    comment: CommentUpdate,
    db: Session = Depends(get_db)
):
    try:
        return comment_service.update_comment(
            db,
            comment_id,
            comment
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# -----------------------------
# Delete Comment
# -----------------------------
@router.delete(
    "/{comment_id}",
    status_code=status.HTTP_200_OK
)
async def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):
    try:
        comment_service.delete_comment(
            db,
            comment_id
        )

        return {
            "message": "Comment deleted successfully"
        }

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )