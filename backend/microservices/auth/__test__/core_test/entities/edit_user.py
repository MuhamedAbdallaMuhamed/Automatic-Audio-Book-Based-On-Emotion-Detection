import unittest

from core.entities import edit_user
from core.entities.exception import *

from config import *
from __test__.core_test.util.util import *
from datetime import datetime


class EditUserTestCase(unittest.TestCase):
    def test_editing_valid_user(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        salt = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        user = edit_user(
            id="1",
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password,
            salt=salt,
            gender=gender,
            birthday=birthday,
            reset_code=None,
            profile_picture_url=None,
            new_first_name=True,
            new_last_name=True,
            new_email=True,
            new_password=True,
            new_phone=True,
            new_birthday=True,
            new_gender=True,
        )

        self.assertEqual(user.id, "1")
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.phone, phone)
        self.assertNotEqual(user.hashed_password, password)
        self.assertEqual(user.gender, gender)
        self.assertIs(user.birthday, birthday)

    def test_editing_user_with_invalid_email(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "l@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        salt = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)

        with self.assertRaises(EmailLengthLimitExceeded) as e:
            edit_user(
                id = "1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_email=True
            )

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "gmail.com"
        with self.assertRaises(EmailNotValid) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_email=True
            )

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmailcom"
        with self.assertRaises(EmailNotValid) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_email=True
            )

    def test_editing_user_with_invalid_first_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        salt = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(NameLengthLimitExceeded) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_first_name=True
            )

        first_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(NameMinLengthBeyondLimit) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_first_name=True
            )

    def test_editing_user_with_invalid_last_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        salt = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(NameLengthLimitExceeded) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_last_name=True,
            )

        last_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(NameMinLengthBeyondLimit) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_last_name=True,
            )

    def test_editing_user_with_invalid_phone(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "01234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        salt = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(PhoneNotValid) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_phone=True
            )

    def test_editing_user_with_invalid_password_length(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH + 1)
        salt = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(PasswordLengthLimitExceeded) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_password=True
            )

        password = generate_lowercase_string_of_length(USER_PASSWORD_MIN_LENGTH - 1)
        with self.assertRaises(PasswordMinLengthBeyondLimit) as e:
            edit_user(
                id="1",
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                salt=salt,
                gender=gender,
                birthday=birthday,
                profile_picture_url=None,
                reset_code=None,
                new_password=True
            )
