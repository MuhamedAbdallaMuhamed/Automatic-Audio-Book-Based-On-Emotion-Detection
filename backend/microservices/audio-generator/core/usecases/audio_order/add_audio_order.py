from core.entities import make_audio_order


def build_add_audio_orders(insert_audio_order):
    def add_audio_order(user_id, title, text, start_page, end_page, cloned) -> bool:
        audio_order = make_audio_order(user_id=user_id, title=title, text=text,
                                       start_page=start_page, end_page=end_page, cloned=cloned)
        return insert_audio_order(audio_order)
    return add_audio_order
