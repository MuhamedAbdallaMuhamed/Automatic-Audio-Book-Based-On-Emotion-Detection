import unittest

from core.entities import make_user
from core.entities.exception import *

from config import *
from __test__.core_test.util.util import *
from datetime import datetime


class MakeUserTestCase(unittest.TestCase):
    def test_creating_valid_user(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        user = make_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password,
            profile_picture_url=None,
            gender=gender,
            birthday=birthday,
        )

        self.assertNotEqual(user.id, "")
        self.assertNotEqual(user.id, None)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.phone, phone)
        self.assertNotEqual(user.hashed_password, password)
        self.assertEqual(user.gender, gender)
        self.assertIs(user.birthday, birthday)

    def test_creating_user_with_invalid_email(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "l@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(EmailLengthLimitExceeded) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "gmail.com"
        with self.assertRaises(EmailNotValid) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmailcom"
        with self.assertRaises(EmailNotValid) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

    def test_creating_user_with_invalid_first_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(NameLengthLimitExceeded) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

        first_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(NameMinLengthBeyondLimit) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

    def test_creating_user_with_invalid_last_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(NameLengthLimitExceeded) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

        last_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(NameMinLengthBeyondLimit) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

    def test_creating_user_with_invalid_phone(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "01234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(PhoneNotValid) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

    def test_creating_user_with_invalid_password_length(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH + 1)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(PasswordLengthLimitExceeded) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )

        password = generate_lowercase_string_of_length(USER_PASSWORD_MIN_LENGTH - 1)
        with self.assertRaises(PasswordMinLengthBeyondLimit) as e:
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                profile_picture_url=None,
                gender=gender,
                birthday=birthday,
            )
