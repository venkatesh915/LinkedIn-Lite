import re


def validate_email(email: str):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.match(pattern, email))


def validate_password(password: str):
    return len(password) >= 8