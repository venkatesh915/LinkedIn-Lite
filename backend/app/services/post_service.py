from sqlalchemy.orm import Session

from app.models.post import Post
from app.repositories.post_repository import PostRepository


post_repo = PostRepository()


def create_post(db: Session, post, user_id: int):
    db_post = Post(
        content=post.content,
        image_url=getattr(post, "image_url", None),
        user_id=user_id
    )

    return post_repo.create_post(db, db_post)


def get_post(db: Session, post_id: int):
    return post_repo.get_post_by_id(db, post_id)


def get_all_posts(db: Session):
    return post_repo.get_all_posts(db)


def get_posts_by_user(db: Session, user_id: int):
    return post_repo.get_posts_by_user(db, user_id)


def update_post(db: Session, post_id: int, post_data, user_id: int):

    db_post = post_repo.get_post_by_id(
        db,
        post_id
    )

    if not db_post:
        return None

    if db_post.user_id != user_id:
        return None

    db_post.content = post_data.content

    if hasattr(post_data, "image_url"):
        db_post.image_url = post_data.image_url

    return post_repo.update_post(db, db_post)


def delete_post(db: Session, post_id: int, user_id: int):

    db_post = post_repo.get_post_by_id(
        db,
        post_id
    )

    if not db_post:
        return None

    if db_post.user_id != user_id:
        return None

    return post_repo.delete_post(db, db_post)