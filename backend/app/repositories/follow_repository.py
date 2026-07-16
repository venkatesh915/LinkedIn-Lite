from sqlalchemy.orm import Session

from app.models.follow import Follow
from app.schemas.follow import FollowCreate, FollowUpdate


class FollowRepository:

    def create_follow(self, db: Session, follow: FollowCreate):
        db_follow = Follow(
            follower_id=follow.follower_id,
            following_id=follow.following_id
        )

        db.add(db_follow)
        db.commit()
        db.refresh(db_follow)

        return db_follow

    def get_follow_by_id(self, db: Session, follow_id: int):
        return (
            db.query(Follow)
            .filter(Follow.id == follow_id)
            .first()
        )

    def get_all_follows(self, db: Session):
        return (
            db.query(Follow)
            .all()
        )

    def get_followers(self, db: Session, user_id: int):
        return (
            db.query(Follow)
            .filter(Follow.following_id == user_id)
            .all()
        )

    def get_following(self, db: Session, user_id: int):
        return (
            db.query(Follow)
            .filter(Follow.follower_id == user_id)
            .all()
        )

    def is_following(self, db: Session, follower_id: int, following_id: int):
        return (
            db.query(Follow)
            .filter(
                Follow.follower_id == follower_id,
                Follow.following_id == following_id
            )
            .first()
        )

    def update_follow(
        self,
        db: Session,
        follow_id: int,
        follow: FollowUpdate
    ):
        db_follow = self.get_follow_by_id(db, follow_id)

        if not db_follow:
            return None

        db_follow.follower_id = follow.follower_id
        db_follow.following_id = follow.following_id

        db.commit()
        db.refresh(db_follow)

        return db_follow

    def delete_follow(self, db: Session, follow_id: int):
        db_follow = self.get_follow_by_id(db, follow_id)

        if not db_follow:
            return False

        db.delete(db_follow)
        db.commit()

        return True