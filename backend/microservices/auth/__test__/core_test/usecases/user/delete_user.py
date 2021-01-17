import unittest

from __test__.core_test.util import *
from core.usecases import delete_user


class DeleteUserTestCase(unittest.TestCase):
    def test_deleting_user_by_id(self):
        user = create_and_add_valid_user()
        ret = delete_user(id=user.id)
        self.assertEqual(ret, True)

    def test_deleting_user_that_does_not_exist(self):
        random_id = generate_random_string_of_length(10)
        ret = delete_user(id=random_id)
        self.assertEqual(ret, True)
