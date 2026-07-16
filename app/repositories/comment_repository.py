from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentUpdate


class CommentRepository:

    def create_comment(self, db: Session, comment: CommentCreate) -> Comment:
        db_comment = Comment(
            content=comment.content,
            user_id=comment.user_id,
            post_id=comment.post_id,
        )

        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)

        return db_comment

    def get_comment_by_id(self, db: Session, comment_id: int) -> Comment | None:
        return (
            db.query(Comment)
            .filter(Comment.id == comment_id)
            .first()
        )

    def get_all_comments(self, db: Session):
        return (
            db.query(Comment)
            .order_by(Comment.created_at.desc())
            .all()
        )

    def get_comments_by_post(self, db: Session, post_id: int):
        return (
            db.query(Comment)
            .filter(Comment.post_id == post_id)
            .order_by(Comment.created_at.asc())
            .all()
        )

    def update_comment(
        self,
        db: Session,
        comment_id: int,
        comment_update: CommentUpdate,
    ) -> Comment | None:

        db_comment = self.get_comment_by_id(db, comment_id)

        if not db_comment:
            return None

        db_comment.content = comment_update.content

        db.commit()
        db.refresh(db_comment)

        return db_comment

    def delete_comment(self, db: Session, comment_id: int) -> bool:
        db_comment = self.get_comment_by_id(db, comment_id)

        if not db_comment:
            return False

        db.delete(db_comment)
        db.commit()

        return True