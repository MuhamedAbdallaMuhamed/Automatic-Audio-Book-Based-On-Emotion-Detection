import unittest

from core.usecases import add_token, is_token_blocked
from __test__.core_test.util.util import *


class TokenTestCase(unittest.TestCase):
    def test_add_token(self):
        token = generate_random_string_of_length(100)
        ret = add_token(token=token)
        self.assertEqual(ret, True)

    def test_token_is_blocked(self):
        token = generate_random_string_of_length(101)
        exist = is_token_blocked(token)
        self.assertEqual(exist, False)
        add_token(token=token)
        exist = is_token_blocked(token)
        self.assertEqual(exist, True)
