from typing import Dict
from flask_jwt_extended import create_access_token
from environs import Env
from flask_sqlalchemy.session import Session
from models.user import UserMethods

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
    return True if user_data else False


def validate_user(db: Session, data: dict) -> Dict:
    """
    validate user for login
    """
    user_data = UserMethods.get_record_with_(
        db,
        email=data.get('email'),
        password=data.get('password'),
        is_active=True
    )
    return user_data


def create_token(db: Session, user_data: Dict) -> Dict:
    """
    Create JWT token
    """
    access_token = create_access_token(identity=user_data["id"])
    return {access_token: access_token}
