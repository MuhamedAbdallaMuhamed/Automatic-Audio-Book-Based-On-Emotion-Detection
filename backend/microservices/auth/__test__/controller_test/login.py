import unittest
import json

from controller import app
from __test__.core_test.util import *


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_login_with_valid_data(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH )
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
            password=password,
            gender=gender,
            birthday=birthday,
        )
        assert ret is True

        res = self.app.post(LOGIN_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email, REQ_USER_PASSWORD_KEY_NAME: password})
        assert res is not None
        assert "200" in res.status
        res = json.loads(res.data)
        assert RES_ACCESS_TOKEN_KEY_NAME in res
        assert RES_REFRESH_TOKEN_KEY_NAME in res

    def test_login_with_invalid_password(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH )
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
            password=password,
            gender=gender,
            birthday=birthday,
        )
        assert ret is True

        password = generate_random_string_of_length(USER_PASSWORD_MAX_LENGTH)
        res = self.app.post(LOGIN_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email, REQ_USER_PASSWORD_KEY_NAME: password})
        assert res is not None
        assert "401" in res.status
        res = json.loads(res.data)
        assert RES_ACCESS_TOKEN_KEY_NAME not in res
        assert RES_REFRESH_TOKEN_KEY_NAME not in res

    def test_login_with_invalid_email(self):
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        password = generate_random_string_of_length(USER_PASSWORD_MAX_LENGTH)
        res = self.app.post(LOGIN_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email, REQ_USER_PASSWORD_KEY_NAME: password})
        assert res is not None
        assert "401" in res.status
        res = json.loads(res.data)
        assert RES_ACCESS_TOKEN_KEY_NAME not in res
        assert RES_REFRESH_TOKEN_KEY_NAME not in res

    def test_token_refresh(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH )
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
            password=password,
            gender=gender,
            birthday=birthday,
        )
        assert ret is True

        res = self.app.post(LOGIN_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email, REQ_USER_PASSWORD_KEY_NAME: password})
        assert res is not None
        assert "200" in res.status
        res = json.loads(res.data)
        assert RES_ACCESS_TOKEN_KEY_NAME in res
        assert RES_REFRESH_TOKEN_KEY_NAME in res

        import time
        acccess_jwt = res[RES_ACCESS_TOKEN_KEY_NAME]
        refresh_jwt = res[RES_REFRESH_TOKEN_KEY_NAME]
        time.sleep(2 * 60 * JWT_ACCESS_TOKEN_LIFETIME_IN_MINUTES)

        res = self.app.get(USER_ABS_ENDPOINT_NAME,
                           headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + acccess_jwt}))
        assert res is not None
        assert "401" in res.status

        res = self.app.post(REFRESH_TOKEN_ABS_ENDPOINT_NAME,
                           headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + refresh_jwt}))
        assert "200" in res.status
        res = json.loads(res.data)
        assert RES_ACCESS_TOKEN_KEY_NAME in res