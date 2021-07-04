import unittest

from __test__.core_test.util.util import *
from core.entities.exception import *


class GetUserTestCase(unittest.TestCase):
    def test_getting_user_by_id(self):
        user1 = create_and_add_valid_user()
        user2 = get_user(id=user1.id)
        self.assertEqual(user1.id, user2.id)
        self.assertEqual(user1.first_name, user2.first_name)
        self.assertEqual(user1.last_name, user2.last_name)
        self.assertEqual(user1.email, user2.email)
        self.assertEqual(user1.phone, user2.phone)
        self.assertEqual(user1.profile_picture_url, user2.profile_picture_url)
        self.assertEqual(user1.hashed_password, user2.hashed_password)
        self.assertEqual(user1.salt, user2.salt)
        self.assertEqual(user1.gender, user2.gender)
        self.assertEqual(user1.birthday, user2.birthday)

    def test_getting_user_by_email(self):
        user1 = create_and_add_valid_user()
        user2 = get_user(email=user1.email)
        self.assertEqual(user1.id, user2.id)
        self.assertEqual(user1.first_name, user2.first_name)
        self.assertEqual(user1.last_name, user2.last_name)
        self.assertEqual(user1.email, user2.email)
        self.assertEqual(user1.phone, user2.phone)
        self.assertEqual(user1.profile_picture_url, user2.profile_picture_url)
        self.assertEqual(user1.hashed_password, user2.hashed_password)
        self.assertEqual(user1.salt, user2.salt)
        self.assertEqual(user1.gender, user2.gender)
        self.assertEqual(user1.birthday, user2.birthday)

    def test_getting_user_by_email_that_does_not_exist(self):
        random_email = generate_random_string_of_length(USER_EMAIL_MAX_LENGTH)
        user = get_user(email=random_email)
        self.assertEqual(user, None)

    def test_getting_user_by_id_that_does_not_exist(self):
        random_id = generate_random_string_of_length(10)
        user = get_user(id=random_id)
        self.assertEqual(user, None)
