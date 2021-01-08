from .add_user import build_add_user
from .update_user import build_update_user


def insert_user(user):
    pass


def update_user(user):
    pass


add_user = build_add_user(insert_user=insert_user)
update_user = build_update_user(update_user=update_user)