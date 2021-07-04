from core.entities import AudioOrder


def build_get_audio_orders(get_user_orders):
    def get_audio_orders(id: str) -> [AudioOrder]:
        return get_user_orders(id)
    return get_audio_orders
