from .user import User
from .exception import *


def build_make_user(id_generator, name_validator, email_validator, password_validator, phone_validator, hash_password, salt_generator):
    def make_user(first_name, last_name, phone, email, password, profile_picture_url, birthday, gender):
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

        salt = salt_generator()
        user = User(
                    id=id_generator(),
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    hashed_password=hash_password(password, salt),
                    salt=salt,
                    profile_picture_url=profile_picture_url,
                    birthday=birthday,
                    gender=gender
                )
        return user
    return make_user
