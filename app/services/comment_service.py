from app.repositories.comment_repository import CommentRepository
from app.schemas.comment import CommentCreate, CommentUpdate

# Create repository instance
comment_repository = CommentRepository()


def create_comment(db, comment: CommentCreate):
    """
    Create a new comment.
    """
    return comment_repository.create_comment(db, comment)


def get_comment_by_id(db, comment_id: int):
    """
    Get a comment by ID.
    """
    return comment_repository.get_comment_by_id(db, comment_id)


def get_all_comments(db):
    """
    Get all comments.
    """
    return comment_repository.get_all_comments(db)


def get_comments_by_post(db, post_id: int):
    """
    Get all comments for a specific post.
    """
    return comment_repository.get_comments_by_post(db, post_id)


def update_comment(db, comment_id: int, comment: CommentUpdate):
    """
    Update an existing comment.
    """
    return comment_repository.update_comment(db, comment_id, comment)


def delete_comment(db, comment_id: int):
    """
    Delete a comment.
    """
    return comment_repository.delete_comment(db, comment_id)