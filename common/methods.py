import base64
import json
import math
from typing import Dict
from environs import Env
from Crypto.Cipher import AES
from passlib.context import CryptContext

env = Env()
env.read_env()


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
COMMON_ENCRYPTION_KEY = env("COMMON_ENCRYPTION_KEY")
COMMON_16_BYTE_IV_FOR_AES = env("COMMON_16_BYTE_IV_FOR_AES")


def hash_password(password: str) -> str:
    password = PWD_CONTEXT.hash(password)
    return password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_common_cipher():
    return AES.new(COMMON_ENCRYPTION_KEY.encode("utf8"),
                   AES.MODE_CBC,
                   COMMON_16_BYTE_IV_FOR_AES.encode("utf8"))


def encrypt_json_with_common_cipher(json_obj: Dict):
    json_string = json.dumps(json_obj)
    common_cipher = get_common_cipher()
    cleartext_length = len(json_string)
    nearest_multiple_of_16 = 16 * math.ceil(cleartext_length / 16)
    padded_cleartext = json_string.rjust(nearest_multiple_of_16)
    raw_ciphertext = common_cipher.encrypt(padded_cleartext.encode("utf8"))
    return base64.b64encode(raw_ciphertext).decode('utf-8')


def decrypt_json_with_common_cipher(json_ciphertext: str):
    common_cipher = get_common_cipher()
    raw_ciphertext = base64.b64decode(json_ciphertext)
    decrypted_message = common_cipher.decrypt(raw_ciphertext)
    return json.loads(decrypted_message.decode('utf-8').strip())
