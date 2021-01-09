from ..entities import User

from .add_user import build_add_user
from .get_user import build_get_user
from .update_user import build_update_user
from .delete_user import build_delete_user

from ..data_access import UserDb


def insert_user(user) -> bool:
    return UserDb.insert_user(user)


def get_user(id) -> User:
    return UserDb.get_user(id)


def update_user(user) -> bool:
    return UserDb.update_user(user)


def delete_user(id) -> bool:
    return UserDb.deleter_user(id)


add_user = build_add_user(insert_user=insert_user)
get_user = build_get_user(get_user=get_user)
update_user = build_update_user(update_user=update_user)
delete_user = build_delete_user(delete_user=delete_user)
