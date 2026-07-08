from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:

    #Create user
    def create_user(self, db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


    #Get user by id
    def get_user_by_id(self, db: Session, user_id: int):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )


    # get user by mail
    def get_user_by_email(self, db: Session, email: str):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )


    # update user
    def update_user(self, db: Session, user: User):
        db.commit()
        db.refresh(user)
        return user


    #delete user
    def delete_user(self, db: Session, user: User):
        db.delete(user)
        db.commit()