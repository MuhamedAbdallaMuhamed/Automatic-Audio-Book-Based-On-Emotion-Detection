from typing import Optional

from core.data_access.admin import db
from ..entities import audio_order
from config import *


class AudioOrderDb:
    @staticmethod
    def insert_book(audioOrder: audio_order) -> bool:
        db.collection(AUDIO_ORDER_COLLECTION_NAME).document(audioOrder.id).set(AudioOrderDb.audio_order_to_dict(audioOrder))
        return True

    @staticmethod
    def get_audio_order_by_id(id: str) -> Optional[audio_order]:
        try:
            a = db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).get().to_dict()
            if a:
                order = audio_order(
                  id=a[AUDIO_ORDER_ID_ENTITY_NAME],
                  title=a[AUDIO_ORDER_TITLE_ENTITY_NAME],
                  user_id=a[AUDIO_ORDER_USER_ID_ENTITY_NAME],
                  text=a[AUDIO_ORDER_TEXT_ENTITY_NAME],
                  start_page=a[AUDIO_ORDER_START_PAGE_ENTITY_NAME],
                  end_page=a[AUDIO_ORDER_END_PAGE_ENTITY_NAME],
                  cloned=a[AUDIO_ORDER_CLONED_ENTITY_NAME],
                  audio_link=a[AUDIO_ORDER_AUDIO_LINK_ENTITY_NAME],
                  chars_names=a[AUDIO_ORDER_CHARACTERS_NAMES_ENTITY_NAME]
                )
                return order
            return None
        except Exception as e:
            print(e)

    @staticmethod
    def update_audio_order(audioOrder: audio_order) -> bool:
        db.collection(AUDIO_ORDER_COLLECTION_NAME).document(audioOrder.id).update(AudioOrderDb.audio_order_to_dict(audioOrder))
        return True

    @staticmethod
    def delete_audio_order(id: str) -> bool:
        db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).delete()
        return True

    @staticmethod
    def audio_order_to_dict(audio_order):
        return {
            AUDIO_ORDER_ID_ENTITY_NAME: audio_order.id,
            AUDIO_ORDER_TEXT_ENTITY_NAME: audio_order.text,
            AUDIO_ORDER_CLONED_ENTITY_NAME: audio_order.cloned,
            AUDIO_ORDER_START_PAGE_ENTITY_NAME: audio_order.start_page,
            AUDIO_ORDER_END_PAGE_ENTITY_NAME: audio_order.end_page,
            AUDIO_ORDER_TITLE_ENTITY_NAME: audio_order.title,
            AUDIO_ORDER_USER_ID_ENTITY_NAME: audio_order.user_id,
            AUDIO_ORDER_AUDIO_LINK_ENTITY_NAME: audio_order.audio_link,
            AUDIO_ORDER_CHARACTERS_NAMES_ENTITY_NAME: audio_order.chars_names,
        }