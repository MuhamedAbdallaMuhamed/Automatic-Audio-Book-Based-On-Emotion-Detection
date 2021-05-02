from .user import User
from .exception import *


def build_edit_user(name_validator, email_validator, password_validator, phone_validator, hash_password, salt_generator):
    def edit_user(id, first_name, last_name, phone, email, password, salt, birthday, gender,
                  profile_picture_url, reset_code, new_first_name = False, new_last_name = False,
                  new_phone = False, new_email = False, new_password = False, new_birthday = False,
                  new_gender = False, new_profile_picture_url = False) -> User:
        # validate first_name
        if new_first_name:
            name_validator(first_name)

        # validate last_name
        if new_last_name:
            name_validator(last_name)

        # validate phone
        if new_phone:
            phone_validator(phone)

        # validate email
        if new_email:
            email_validator(email)

        # validate password
        if new_password:
            password_validator(password)

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
                    gender=gender,
                    password_reset_code=reset_code
                )
        return user
    return edit_user
