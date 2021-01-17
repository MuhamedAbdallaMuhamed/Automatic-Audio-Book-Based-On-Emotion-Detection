import unittest
from datetime import datetime

from __test__.core_test.util.util import *
from core.usecases import add_user
from core.entities.exception import *


class AddUserTestCase(unittest.TestCase):
    def test_inserting_valid_user(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        ret = add_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password,            gender=gender,
            birthday=birthday,
        )
        self.assertEqual(ret, True)

    def test_inserting_user_with_invalid_email(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "l@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(EmailLengthLimitExceeded) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "gmail.com"
        with self.assertRaises(EmailNotValid) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmailcom"
        with self.assertRaises(EmailNotValid) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

    def test_inserting_user_with_invalid_first_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(NameLengthLimitExceeded) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

        first_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(NameMinLengthBeyondLimit) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

    def test_inserting_user_with_invalid_last_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(NameLengthLimitExceeded) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

        last_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(NameMinLengthBeyondLimit) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

    def test_inserting_user_with_invalid_phone(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "01234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(PhoneNotValid) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

    def test_inserting_user_with_invalid_password_length(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH + 1)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(PasswordLengthLimitExceeded) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )

        password = generate_lowercase_string_of_length(USER_PASSWORD_MIN_LENGTH - 1)
        with self.assertRaises(PasswordMinLengthBeyondLimit) as e:
            add_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday,
            )
