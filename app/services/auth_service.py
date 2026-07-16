from app.repositories.user_repository import UserRepository
from app.utils.hashing import verify_password
from app.core.security import create_access_token


user_repository = UserRepository()


def login_user(db, email: str, password: str):

    # Get user by email
    user = user_repository.get_user_by_email(
        db,
        email
    )

    if not user:
        raise Exception("Invalid email or password")


    # Verify password
    if not verify_password(
        password,
        user.password
    ):
        raise Exception("Invalid email or password")


    # Create JWT token
    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "email": user.email
        }
    )


    return {
        "access_token": access_token,
        "token_type": "bearer"
    }