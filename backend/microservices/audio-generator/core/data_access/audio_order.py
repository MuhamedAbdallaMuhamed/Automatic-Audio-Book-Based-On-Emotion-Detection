from typing import Optional

from core.data_access.admin import db
from core.entities import AudioOrder
from config import *
from .admin import bucket


class AudioOrderDb:
    @staticmethod
    def insert_audio_order(audioOrder: AudioOrder) -> bool:
        print(AudioOrderDb.audio_order_to_dict(audioOrder))
        db.collection(AUDIO_ORDER_COLLECTION_NAME).document(audioOrder.id).set(
            AudioOrderDb.audio_order_to_dict(audioOrder))
        return audioOrder

    @staticmethod
    def add_audio_file(id, file_path):
        blob = bucket.blob('audios/' + id + '.wav')
        blob.upload_from_filename(filename=file_path, timeout=300)
        blob.make_public()
        os.remove(file_path)
        AudioOrderDb.update_audio_order(id, audio_link=blob.public_url, chars_names=None, scripts=None)

    @staticmethod
    def get_audio_order_by_id(id):
        a = db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).get().to_dict()
        audio_order = AudioOrder(
            id=a[AUDIO_ORDER_ID_ENTITY_NAME],
            title=a[AUDIO_ORDER_TITLE_ENTITY_NAME],
            user_id=a[AUDIO_ORDER_USER_ID_ENTITY_NAME],
            text=a[AUDIO_ORDER_TEXT_ENTITY_NAME],
            start_page=a[AUDIO_ORDER_START_PAGE_ENTITY_NAME],
            end_page=a[AUDIO_ORDER_END_PAGE_ENTITY_NAME],
            cloned=a[AUDIO_ORDER_CLONED_ENTITY_NAME],
            audio_link=a[AUDIO_ORDER_AUDIO_LINK_ENTITY_NAME],
            chars_names=a[AUDIO_ORDER_CHARACTERS_NAMES_ENTITY_NAME],
            scripts=AudioOrderDb.from_dict_to_scripts(a)
        )
        return audio_order

    @staticmethod
    def get_user_audio_orders(user_id: str) -> Optional[AudioOrder]:
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
                chars_names=a[AUDIO_ORDER_CHARACTERS_NAMES_ENTITY_NAME],
                scripts=AudioOrderDb.from_dict_to_scripts(a)
            )
            audio_orders.append(audio_order)
        return audio_orders

    @staticmethod
    def update_audio_order(id, audio_link, chars_names, scripts, sentences=None) -> bool:
        if audio_link and chars_names:
            db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).update({
                AUDIO_ORDER_CHARACTERS_NAMES_ENTITY_NAME: chars_names,
                AUDIO_ORDER_AUDIO_LINK_ENTITY_NAME: audio_link
            })
        if audio_link:
            db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).update({
                AUDIO_ORDER_AUDIO_LINK_ENTITY_NAME: audio_link
            })
        if chars_names:
            db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).update({
                AUDIO_ORDER_CHARACTERS_NAMES_ENTITY_NAME: chars_names,
            })
        if scripts:
            db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).update({
                AUDIO_ORDER_AUDIO_SCRIPTS_ENTITY_NAME: AudioOrderDb.to_scripts(scripts),
            })
        if sentences:
            db.collection(AUDIO_ORDER_COLLECTION_NAME).document(id).update({
                AUDIO_ORDER_TEXT_ENTITY_NAME: sentences,
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
            AUDIO_ORDER_AUDIO_SCRIPTS_ENTITY_NAME: AudioOrderDb.to_scripts(audio_order.scripts)
        }

    @staticmethod
    def to_scripts(scripts):
        return None if scripts is None else {char_name: [{'0': t[0], '1': t[1]} for t in scripts[char_name]] for
                                             char_name in scripts}

    @staticmethod
    def from_dict_to_scripts(a):
        if not a or AUDIO_ORDER_AUDIO_SCRIPTS_ENTITY_NAME not in a or a[AUDIO_ORDER_AUDIO_SCRIPTS_ENTITY_NAME] is None:
            return None
        x = {char_name: [(dic['0'], dic['1']) for dic in a[AUDIO_ORDER_AUDIO_SCRIPTS_ENTITY_NAME][char_name]] for
             char_name in a[AUDIO_ORDER_AUDIO_SCRIPTS_ENTITY_NAME]}
        return x
