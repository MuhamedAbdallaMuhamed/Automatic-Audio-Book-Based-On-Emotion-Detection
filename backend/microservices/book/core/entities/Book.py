class Book:
    def __init__(self, id, name, book_hash, book_path, sentence_features):
        self.__id = id
        self.__name = name
        self.__book_hash = book_hash
        self.__book_path = book_path
        self.__sentence_features = sentence_features

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def book_hash(self):
        return self.__book_hash

    @property
    def book_path(self):
        return self.__book_path

    @property
    def sentence_features(self):
        return self.__sentence_features
