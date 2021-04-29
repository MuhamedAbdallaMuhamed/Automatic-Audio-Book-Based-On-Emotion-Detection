from .audio_order import AudioOrder
from .exception import *


def build_make_user(id_generator):
    def make_user(user_id, title, text, start_page, end_page, cloned):
        # validate first_name
        name_validator(first_name)
        # validate last_name
        name_validator(last_name)
        # validate phone
        phone_validator(phone)
        # validate email
        email_validator(email)
        # validate password
        password_validator(password)

        user = AudioOrder(
                    id=id_generator(),
                    user_id=user_id,
                    title=title,
                    text=text,
                    start_page=start_page,
                    end_page=end_page,
                    cloned=cloned,
                    audio_link=None,
                    chars_names=None
                )
        return user
    return make_user
