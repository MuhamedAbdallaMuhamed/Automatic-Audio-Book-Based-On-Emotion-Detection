from ..entities import User


def build_get_user(get_user):
    def get_user(id: str) -> User:
        return get_user(id)
    return get_user
