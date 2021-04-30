def build_update_audio_order(update_audio_order_db):
    def update_audio_order(id, audio_link, chars_names) -> bool:
        return update_audio_order_db(id, audio_link, chars_names)
    return update_audio_order
