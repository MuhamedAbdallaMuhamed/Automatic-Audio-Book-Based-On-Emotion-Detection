from .user import User
from .exception import *


def build_edit_user(name_validator, email_validator, password_validator, phone_validator, hash_password, salt_generator):
    def edit_user(id, first_name, last_name, phone, email, password, salt, profile_picture_url, birthday, gender
                  ,new_first_name = False, new_last_name = False, new_phone = False, new_email = False,
                  new_password = False, new_profile_picture_url = False, new_birthday = False, new_gender = False) -> User:
        # validate first_name
        if new_first_name and not name_validator(first_name):
            raise NameLengthLimitExceeded

        # validate last_name
        if new_last_name and not name_validator(last_name):
            raise NameLengthLimitExceeded

        # validate phone
        if new_phone and not phone_validator(phone):
            raise PhoneNotValid

        # validate email
        if new_email and not email_validator(email):
            raise EmailNotValid

        # validate password
        if new_pasword and not password_validator(email):
            raise PasswordLengthLimitExceeded

        salt = salt_generator() if new_password else salt
        user = User(
                    id=id,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    hashed_password=hash_password(password, salt) if new_password else password,
                    salt=salt,
                    profile_picture_url=profile_picture_url,
                    birthday=birthday,
                    gender=gender
                )
        return user
    return edit_user
