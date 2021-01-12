class User:
    def __init__(self, id, first_name, last_name, phone, email, hashed_password, salt, profile_picture_url, birthday, gender):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email
        self.__hashed_password = hashed_password
        self.__profile_picture_url = profile_picture_url
        self.__salt = salt
        self.__birthday = birthday
        self.__gender = gender

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def hashed_password(self):
        return self.__hashed_password

    @property
    def salt(self):
        return self.__salt

    @property
    def profile_picture_url(self):
        return self.__profile_picture_url

    @property
    def birthday(self):
        return self.__birthday

    @property
    def gender(self):
        return self.__gender
