from core.usecases.user import *

from ..data_access import *


def insert_audio_order(audio_order) -> bool:
    return AudioOrderDb.insert_audio_order(audio_order)


def get_user_orders(user_id) -> AudioOrder:
    return AudioOrderDb.get_user_audio_orders(user_id)


def update_audio_order(id, audio_link, chars_names, scripts) -> bool:
    return AudioOrderDb.update_audio_order(id, audio_link, chars_names, scripts)


add_audio_order = build_add_audio_orders(insert_audio_order=insert_audio_order)
get_audio_orders = build_get_audio_orders(get_user_orders=get_user_orders)
update_audio_order = build_update_audio_order(update_audio_order_db=update_audio_order)
get_audio_order = AudioOrderDb.get_audio_order_by_id
