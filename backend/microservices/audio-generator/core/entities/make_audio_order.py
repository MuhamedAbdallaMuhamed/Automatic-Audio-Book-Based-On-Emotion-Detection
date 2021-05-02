from .audio_order import AudioOrder


def build_make_audio_order(id_generator, title_validator, page_number_validator):
    def make_audio_order(user_id, title, text, start_page, end_page, cloned):
        # validate title
        title_validator(title)
        # validate start_page
        page_number_validator(start_page)
        # validate end_page
        page_number_validator(end_page)

        user = AudioOrder(
                    id=id_generator(),
                    user_id=user_id,
                    title=title,
                    text=text,
                    start_page=start_page,
                    end_page=end_page,
                    cloned=cloned,
                    audio_link=None,
                    chars_names=None,
                    scripts=None
                )
        return user
    return make_audio_order
