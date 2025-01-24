import bcrypt


def hash_password(password: str) -> tuple[str, str]:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    data = {'password': bcrypt.hashpw(pwd_bytes, salt).decode(), 'salt': salt.decode()}
    return data['password'], data['salt']
