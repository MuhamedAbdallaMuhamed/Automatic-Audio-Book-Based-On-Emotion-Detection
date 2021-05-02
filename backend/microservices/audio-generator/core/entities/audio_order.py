class AudioOrder:
    def __init__(self, id, user_id, title, text, start_page, end_page, cloned, audio_link, chars_names, scripts):
        self.__id = id
        self.__user_id = user_id
        self.__title = title
        self.__text = text
        self.__start_page = start_page
        self.__end_page = end_page
        self.__audio_link = audio_link
        self.__cloned = cloned
        self.__scripts = scripts
        self.__chars_names = chars_names if chars_names is None else {char_name: '' for char_name in chars_names}

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def title(self):
        return self.__title

    @property
    def start_page(self):
        return self.__start_page

    @property
    def text(self):
        return self.__text

    @property
    def end_page(self):
        return self.__end_page

    @property
    def cloned(self):
        return self.__cloned

    @property
    def audio_link(self):
        return self.__audio_link

    @property
    def scripts(self):
        return self.__scripts

    @property
    def chars_names(self):
        return self.__chars_names