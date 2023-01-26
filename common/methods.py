from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    password = PWD_CONTEXT.hash(password)
    return password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)
