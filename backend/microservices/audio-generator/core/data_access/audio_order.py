from typing import Optional

from core.data_access.admin import db
from core.entities import AudioOrder
from config import *


class AudioOrderDb:
    @staticmethod
    def insert_audio_order(audioOrder: AudioOrder) -> bool:
        print(AudioOrderDb.audio_order_to_dict(audioOrder))
        db.collection(AUDIO_ORDER_COLLECTION_NAME).document(audioOrder.id).set(AudioOrderDb.audio_order_to_dict(audioOrder))
        return audioOrder

    @staticmethod
    def get_user_audio_orders(user_id: str) -> Optional[AudioOrder]:
        try:
            audio_orders = []
            res = db.collection(AUDIO_ORDER_COLLECTION_NAME).where(AUDIO_ORDER_USER_ID_ENTITY_NAME, '==', user_id).stream()
            for audio_order in res:
                a = audio_order.to_dict()
                audio_order = AudioOrder(
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
                audio_orders.append(audio_order)
            return audio_orders
        except Exception as e:
            print(e)

    @staticmethod
    def update_audio_order(id, audio_link, chars_names) -> bool:
        if audio_link and chars_names:
            db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).update({
                AUDIO_ORDER_CHARACTERS_NAMES_ENTITY_NAME: chars_names,
                AUDIO_ORDER_AUDIO_LINK_ENTITY_NAME: audio_link
            })
        elif audio_link:
            db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).update({
                AUDIO_ORDER_AUDIO_LINK_ENTITY_NAME: audio_link
            })
        elif chars_names:
            db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).update({
                AUDIO_ORDER_CHARACTERS_NAMES_ENTITY_NAME: chars_names,
            })
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