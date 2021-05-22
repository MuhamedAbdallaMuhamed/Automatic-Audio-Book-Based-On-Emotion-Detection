from core.entities import Sentence
from config import *
from .admin import db


class BookDb:

    @staticmethod
    def insert_book(hashing, sentences_list: [Sentence]) -> bool:
        db.collection(BOOK_COLLECTION_NAME).document(hashing).set(BookDb.sentences_to_dict(sentences_list))

    @staticmethod
    def get_book(hashing) -> [Sentence]:
        book_ref = db.collection(BOOK_COLLECTION_NAME).document(hashing).get()
        if book_ref.exists:
            return BookDb.dict_to_sentences(book_ref.to_dict())
        return None

    @staticmethod
    def sentences_to_dict(sentences: [Sentence]):
        res = {}
        for sentence in sentences:
            res[sentence.pos] = {
                BOOK_SENTENCE_ENTITY_NAME: sentence.text,
                BOOK_CHAR_NAME_ENTITY_NAME: sentence.character_name
            }

    @staticmethod
    def dict_to_sentences(book_dict: dict):
        sentences = []
        for pos in book_dict.keys():
            sentence = book_dict.get(pos)
            sentences.append(Sentence(
                sentence[BOOK_SENTENCE_ENTITY_NAME],
                sentence[BOOK_CHAR_NAME_ENTITY_NAME],
                pos=pos))

        sentences.sort(key=lambda x, y: x.pos - y.pos)