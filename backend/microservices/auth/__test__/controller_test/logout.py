import unittest
import json

from controller import app
from __test__.core_test.util import *


class LogoutTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_logout_with_valid_jwt(self):
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
        acccess_jwt = res[RES_ACCESS_TOKEN_KEY_NAME]
        refresh_jwt = res[RES_REFRESH_TOKEN_KEY_NAME]

        res = self.app.get(USER_ABS_ENDPOINT_NAME,
                           headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + acccess_jwt}))
        assert res is not None
        assert "200" in res.status
        res = json.loads(res.data)
        assert RES_USER_FIRST_NAME_KEY_NAME in res
        assert RES_USER_LAST_NAME_KEY_NAME in res
        assert RES_USER_EMAIL_KEY_NAME in res
        assert RES_USER_ID_KEY_NAME in res
        assert RES_USER_PROFILE_PICTURE_URL_KEY_NAME in res

        res = self.app.delete(LOGOUT_ABS_ENDPOINT_NAME,
                           headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + acccess_jwt}))
        assert "200" in res.status

        res = self.app.get(USER_ABS_ENDPOINT_NAME,
                           headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + acccess_jwt}))
        assert res is not None
        assert "401" in res.status
