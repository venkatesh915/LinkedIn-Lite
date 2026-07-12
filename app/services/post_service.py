from sqlalchemy.orm import Session
from app.models.post import Post
from app.repositories.post_repository import PostRepository

post_repo = PostRepository()


def create_post(db: Session, post: Post):
    return post_repo.create_post(db, post)


def get_post(db: Session, post_id: int):
    return post_repo.get_post_by_id(db, post_id)


def get_all_posts(db: Session):
    return post_repo.get_all_posts(db)


def get_posts_by_user(db: Session, user_id: int):
    return post_repo.get_posts_by_user(db, user_id)


def update_post(db: Session, post: Post):
    return post_repo.update_post(db, post)


def delete_post(db: Session, post: Post):
    return post_repo.delete_post(db, post)