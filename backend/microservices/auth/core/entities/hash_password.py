import hashlib


def hash_password(password: str, salt: str):
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
