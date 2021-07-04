from core.entities import User


def build_get_user(get_user_by_id, get_user_by_email):
    def get_user(id: str = None, email: str = None) -> User:
        return get_user_by_id(id) if id else get_user_by_email(email)
    return get_user
