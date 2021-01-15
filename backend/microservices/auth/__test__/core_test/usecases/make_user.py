import unittest

from core.entities import make_user
from config import *
from .util import *
from datetime import datetime


class MakeUserTestCase(unittest.TestCase):
    def create_valid_user(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "01234567890"
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
        self.assertEqual(user.password, password)
        self.assertEqual(user.gender, gender)
        self.assertIs(user.birthday, birthday)


if __name__ == '__main__':
    unittest.main()
