import unittest

from core.usecases import update_user
from core.usecases.user.exception import UserDoesNotExist
from core.entities.exception import *
from __test__.core_test.util.util import *
from datetime import datetime


class UpdateUserTestCase(unittest.TestCase):
    def test_updating_valid_user(self):
        user = create_and_add_valid_user()
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        ret = update_user(
            id=user.id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password,
            gender=gender,
            birthday=birthday
        )
        self.assertEqual(ret, True)

    def test_updating_user_that_does_not_exist(self):
        random_id = generate_random_string_of_length(10)
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        with self.assertRaises(UserDoesNotExist) as e:
            update_user(
                id=random_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
                gender=gender,
                birthday=birthday
            )

    def test_updating_user_with_invalid_email(self):
        user = create_and_add_valid_user()
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "l@gmail.com"
        with self.assertRaises(EmailLengthLimitExceeded) as e:
            update_user(id=user.id, email=email)

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "gmail.com"
        with self.assertRaises(EmailNotValid) as e:
            update_user(id=user.id, email=email)

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmailcom"
        with self.assertRaises(EmailNotValid) as e:
            update_user(id=user.id, email=email)

        email = user.email
        user = create_and_add_valid_user()
        with self.assertRaises(EmailAlreadyExist) as e:
            update_user(id=user.id, email=email)

    def test_updating_user_with_invalid_first_name(self):
        user = create_and_add_valid_user()
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        with self.assertRaises(NameLengthLimitExceeded) as e:
            update_user(id=user.id, first_name=first_name)

        first_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(NameMinLengthBeyondLimit) as e:
            update_user(id=user.id, first_name=first_name)

    def test_updating_user_with_invalid_last_name(self):
        user = create_and_add_valid_user()
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        with self.assertRaises(NameLengthLimitExceeded) as e:
            update_user(id=user.id, last_name=last_name)

        last_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(NameMinLengthBeyondLimit) as e:
            update_user(id=user.id, last_name=last_name)

    def test_updating_user_with_invalid_phone(self):
        user = create_and_add_valid_user()
        phone = "01234567890"
        with self.assertRaises(PhoneNotValid) as e:
            update_user(id=user.id, phone=phone)

    def test_updating_user_with_invalid_password_length(self):
        user = create_and_add_valid_user()
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH + 1)
        with self.assertRaises(PasswordLengthLimitExceeded) as e:
            update_user(id=user.id, password=password)

        password = generate_lowercase_string_of_length(USER_PASSWORD_MIN_LENGTH - 1)
        with self.assertRaises(PasswordMinLengthBeyondLimit) as e:
            update_user(id=user.id, password=password)
