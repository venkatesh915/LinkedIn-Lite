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
    db_user = user_repository.get_user_by_id(db, user_id)

    if not db_user:
        return None

    if user.full_name is not None:
        db_user.full_name = user.full_name

    if user.bio is not None:
        db_user.bio = user.bio

    if hasattr(user, "headline") and user.headline is not None:
        db_user.headline = user.headline

    if hasattr(user, "profile_image_url") and user.profile_image_url is not None:
        db_user.profile_image = user.profile_image_url

    return user_repository.update_user(db, db_user)


# Delete User
def delete_user(db, user_id: int):
    db_user = user_repository.get_user_by_id(db, user_id)

    if not db_user:
        return None

    user_repository.delete_user(db, db_user)
    return True