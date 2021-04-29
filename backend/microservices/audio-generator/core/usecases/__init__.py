from core.usecases.user import *

from ..data_access import *


def insert_audio_order(audio_order) -> bool:
    return AudioOrderDb.insert_AudioOrder(audio_order)


def get_user_orders(id) -> AudioOrder:
    return AudioOrderDb.get_user_orders(id)


def update_audio_order(id, audiolink, charsnames) -> bool:
    return AudioOrderDb.update_audio_order(id, audiolink, charsnames)


add_user = build_add_audio_orders(insert_audio_order=insert_audio_order)
get_user = build_get_audio_orders(get_user_orders=get_user_orders)
update_user = build_update_audio_order(update_audio_order=update_audio_order)
