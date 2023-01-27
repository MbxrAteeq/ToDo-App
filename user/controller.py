from typing import Dict

from environs import Env
from flask_jwt_extended import create_access_token
from sqlalchemy.orm import Session

from common.methods import verify_password
from models.user import UserMethods, User

env = Env()
env.read_env()


def check_user_already_exists(db: Session, email: str) -> Dict:
    """
    Check if user already exists
    """
    user_data = UserMethods.get_record_with_(db, email=email)
    return user_data


def create_user(db: Session, data: Dict) -> bool:
    """
    Create user
    """
    user_data = UserMethods.create_record(data, db)
    return bool(user_data)


def validate_user(db: Session, data: dict) -> User:
    """
    validate user for login
    """
    user_data = UserMethods.get_record_with_(
        db, email=data.get("email"), is_active=True
    )
    if user_data:
        verify_password(data.get("password"), user_data.password)
    return user_data


def create_token(user_data: User) -> Dict:
    """
    Create JWT token
    """
    access_token = create_access_token(identity=user_data.id)
    return {"status": "Success", "access_token": access_token}
