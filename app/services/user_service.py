from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.hashing import hash_password

user_repo = UserRepository()


def register_user(db: Session, user: User):

    existing_user = user_repo.get_user_by_email(db, user.email)

    if existing_user:
        raise Exception("Email already exists")

    user.password = hash_password(user.password)

    return user_repo.create_user(db, user)


def get_user(db: Session, user_id: int):
    return user_repo.get_user_by_id(db, user_id)


def get_all_users(db: Session):
    return user_repo.get_all_users(db)


def update_user(db: Session, user: User):
    return user_repo.update_user(db, user)


def delete_user(db: Session, user: User):
    return user_repo.delete_user(db, user)