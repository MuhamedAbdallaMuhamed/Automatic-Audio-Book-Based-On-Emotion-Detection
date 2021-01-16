from datetime import datetime

from ..entities import User

from core.usecases.user import *
from core.usecases.token import *

from ..data_access import *


def add_image_to_storage(user_id, image_data):
    return UserDb.add_image_to_storage(user_id, image_data)


def insert_user(user) -> bool:
    return UserDb.insert_user(user)


def get_user_by_id(id) -> User:
    return UserDb.get_user_by_id(id)


def get_user_by_email(email) -> User:
    return UserDb.get_user_by_email(email)


def update_user(user) -> bool:
    return UserDb.update_user(user)


def delete_user(id) -> bool:
    return UserDb.deleter_user(id)


add_user = build_add_user(insert_user=insert_user)
get_user = build_get_user(get_user_by_id=get_user_by_id, get_user_by_email=get_user_by_email)
update_user = build_update_user(update_user=update_user, add_image_to_storage=add_image_to_storage)
delete_user = build_delete_user(delete_user=delete_user)


def insert_token(token: str) -> bool:
    return TokenDb.insert_token(token=token)


def is_token_exist(token: str) -> bool:
    return TokenDb.is_token_exist(token=token)


is_token_blocked = build_is_token_exist(is_token_exist=is_token_exist)
add_token = build_add_token(insert_token=insert_token)
