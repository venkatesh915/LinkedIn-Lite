from sqlalchemy.orm import Session

from app.models.like import Like
from app.schemas.like import LikeCreate, LikeUpdate


class LikeRepository:

    def create_like(self, db: Session, like: LikeCreate):
        db_like = Like(
            user_id=like.user_id,
            post_id=like.post_id
        )

        db.add(db_like)
        db.commit()
        db.refresh(db_like)

        return db_like

    def get_like_by_id(self, db: Session, like_id: int):
        return (
            db.query(Like)
            .filter(Like.id == like_id)
            .first()
        )

    def get_all_likes(self, db: Session):
        return db.query(Like).all()

    def get_post_likes(self, db: Session, post_id: int):
        return (
            db.query(Like)
            .filter(Like.post_id == post_id)
            .all()
        )

    def get_user_likes(self, db: Session, user_id: int):
        return (
            db.query(Like)
            .filter(Like.user_id == user_id)
            .all()
        )

    def is_liked(self, db: Session, user_id: int, post_id: int):
        return (
            db.query(Like)
            .filter(
                Like.user_id == user_id,
                Like.post_id == post_id
            )
            .first()
        )

    def update_like(self, db: Session, like_id: int, like: LikeUpdate):
        db_like = self.get_like_by_id(db, like_id)

        if not db_like:
            return None

        db_like.user_id = like.user_id
        db_like.post_id = like.post_id

        db.commit()
        db.refresh(db_like)

        return db_like

    def delete_like(self, db: Session, like_id: int):
        db_like = self.get_like_by_id(db, like_id)

        if not db_like:
            return False

        db.delete(db_like)
        db.commit()

        return True