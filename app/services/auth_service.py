from app.repositories.user_repository import get_user_by_email
from app.utils.hashing import verify_password
from app.core.security import create_access_token


def login_user(db, email: str, password: str):
    """
    Authenticate user and generate JWT token.
    """

    # Check if user exists
    user = get_user_by_email(db, email)

    if not user:
        raise Exception("Invalid email")

    # Verify password
    if not verify_password(password, user.password):
        raise Exception("Invalid password")

    # Generate JWT Token
    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "email": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }


def get_current_user(db, email: str):
    """
    Return logged-in user details.
    """
    return get_user_by_email(db, email)