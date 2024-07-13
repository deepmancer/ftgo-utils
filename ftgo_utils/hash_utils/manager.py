from typing import Optional, Protocol, Tuple, Union

from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib.hashers.bcrypt import BcryptHasher


class HashFNFactory:
    _instance = None
    @staticmethod
    def get_or_create():
        if HashFNFactory._instance is None:
            HashFNFactory._instance = PasswordHash(
                [
                    Argon2Hasher(),
                    BcryptHasher(),
                ],
            )
        return HashFNFactory._instance


def verify_and_update(value: str, hashed_value: str) -> Tuple[bool, Union[str, None]]:
    hash_fn = HashFNFactory.get_or_create()
    return hash_fn.verify_and_update(value, hashed_value)

def verify(value: str, hashed_value: str) -> bool:
    hash_fn = HashFNFactory.get_or_create()
    return hash_fn.verify(value, hashed_value)

def hash_value(value: str) -> str:
    hash_fn = HashFNFactory.get_or_create()
    return hash_fn.hash(value)
