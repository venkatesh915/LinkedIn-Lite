from sqlalchemy.orm import Session
from app.models.post import Post


class PostRepository:

    #create post
    def create_post(self, db: Session, post: Post):
        db.add(post)
        db.commit()
        db.refresh(post)
        return post


    #get post by id
    def get_post_by_id(self, db: Session, post_id: int):
        return (
            db.query(Post)
            .filter(Post.id == post_id)
            .first()
        )


    # get all post
    def get_all_posts(self, db: Session):
        return db.query(Post).all()


    # get post by user
    def get_posts_by_user(self, db: Session, user_id: int):
        return (
            db.query(Post)
            .filter(Post.user_id == user_id)
            .all()
        )


    # update post
    def update_post(self, db: Session, post: Post):
        db.commit()
        db.refresh(post)
        return post


    #delete post
    def delete_post(self, db: Session, post: Post):
        db.delete(post)
        db.commit()