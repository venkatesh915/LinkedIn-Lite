from app.repositories.like_repository import LikeRepository
from app.schemas.like import LikeCreate

like_repository = LikeRepository()


def like_post(db, user_id: int, post_id: int):
    like = LikeCreate(
        user_id=user_id,
        post_id=post_id
    )
    return like_repository.create_like(db, like)


def unlike_post(db, user_id: int, post_id: int):
    return like_repository.delete_like(
        db,
        user_id,
        post_id
    )


def get_post_likes(db, post_id: int):
    return like_repository.get_post_likes(db, post_id)


def get_user_likes(db, user_id: int):
    return like_repository.get_user_likes(db, user_id)


def is_liked(db, user_id: int, post_id: int):
    return like_repository.is_liked(
        db,
        user_id,
        post_id
    )