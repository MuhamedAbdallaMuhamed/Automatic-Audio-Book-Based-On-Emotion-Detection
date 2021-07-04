import unittest
import json

from controller import app
from __test__.core_test.util import *


class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_register_with_valid_data(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH )
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)

        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert res is not None
        assert "201" in res.status

        res = self.app.post(LOGIN_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email, REQ_USER_PASSWORD_KEY_NAME: password})
        assert res is not None
        assert "200" in res.status
        res = json.loads(res.data)
        assert RES_ACCESS_TOKEN_KEY_NAME in res
        assert RES_REFRESH_TOKEN_KEY_NAME in res

    def test_register_user_with_invalid_email(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "l@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "gmail.com"
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmailcom"
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

    def test_register_user_with_invalid_first_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

        first_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

    def test_register_user_with_invalid_last_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

        last_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

    def test_register_user_with_invalid_phone(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "01234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

    def test_register_user_with_invalid_password_length(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH + 1)
        gender = "m"
        birthday = datetime(1999, 7, 24)
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status

        password = generate_lowercase_string_of_length(USER_PASSWORD_MIN_LENGTH - 1)
        res = self.app.post(REGISTER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_USER_PASSWORD_KEY_NAME: password,
                                  REQ_USER_FIRST_NAME_KEY_NAME: first_name,
                                  REQ_USER_LAST_NAME_KEY_NAME: last_name,
                                  REQ_USER_BIRTHDAY_KEY_NAME: birthday.strftime(REQ_USER_BIRTHDAY_FORMAT),
                                  REQ_USER_PHONE_KEY_NAME: phone,
                                  REQ_USER_GENDER_KEY_NAME: gender})
        assert "400" in res.status
