import sys
from os import path
sys.path.append(path.realpath(path.join(path.dirname(__file__), '../..')))


from .make_audio_order import build_make_audio_order
from .audio_order import *
from .exception import *
from .book_parsing import *
from .sentence import *


def title_validator(title: str):
    from config import BOOK_TITLE_MIN_LENGTH, BOOK_TITLE_MAX_LENGTH
    if len(title) > BOOK_TITLE_MAX_LENGTH:
        raise BookTitleLengthLimitExceeded

    if len(title) < BOOK_TITLE_MIN_LENGTH:
        raise BookTitleMinLengthBeyondLimit

    return True


def page_number_validator(pageNumber: int):
    if pageNumber < 1:
        raise PageNumberBeyondLimit
    return True


def id_generator():
    import uuid
    return uuid.uuid4().hex


make_audio_order = build_make_audio_order(
    id_generator=id_generator,
    title_validator=title_validator,
    page_number_validator=page_number_validator)