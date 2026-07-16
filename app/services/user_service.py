from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.hashing import hash_password

from app.repositories.user_repository import UserRepository
user_repository = UserRepository()
# Create User
def create_user(db, user: UserCreate):
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        username=user.username,
        password=hash_password(user.password)
    )

    return user_repository.create_user(db, db_user)


# Get User by ID
def get_user_by_id(db, user_id: int):
    return user_repository.get_user_by_id(db, user_id)


# Get All Users
def get_all_users(db):
    return user_repository.get_all_users(db)


# Update User
def update_user(db, user_id: int, user: UserUpdate):
    return user_repository.update_user(db, user_id, user)


# Delete User
def delete_user(db, user_id: int):
    return user_repository.delete_user(db, user_id)