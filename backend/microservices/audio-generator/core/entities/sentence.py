
class Sentence:
    def __init__(self, text, pos, direction, char_name: str = None):
        self.__text = text
        self.__pos = pos
        self.__sound_file_path = None
        self.__char_name = char_name
        self.__direction = direction

    def set_sound_file_path(self, path):
        self.__sound_file_path = path

    def set_character(self, char_name):
        self.__char_name = char_name

    @property
    def text(self):
        return self.__text

    @property
    def pos(self):
        return self.__pos

    @property
    def sound_file_path(self):
        return self.__sound_file_path

    @property
    def character_name(self):
        return self.__char_name

    @property
    def direction(self):
        return self.__direction
