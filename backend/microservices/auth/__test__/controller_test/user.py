import unittest
import json

from controller import app
from __test__.core_test.util import *


class UserEndpointTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_user_data_with_valid_jwt(self):
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
        assert RES_USER_PHONE_KEY_NAME in res
        assert RES_USER_GENDER_KEY_NAME in res
        assert RES_USER_BIRTHDAY_KEY_NAME in res

    def test_get_user_data_with_invalid_jwt(self):
        acccess_jwt = generate_random_string_of_length(100)
        res = self.app.get(USER_ABS_ENDPOINT_NAME,
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + acccess_jwt}))
        assert res is not None
        assert "422" in res.status

    def test_update_user_with_invalid_email(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
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
        access_jwt = res[RES_ACCESS_TOKEN_KEY_NAME]

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "1@gmail.com"
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "gmail.com"
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmailcom"
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
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

        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                           data={REQ_USER_EMAIL_KEY_NAME: email},
                           headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

    def test_update_user_with_invalid_first_name(self):
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
        access_jwt = res[RES_ACCESS_TOKEN_KEY_NAME]

        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_FIRST_NAME_KEY_NAME: first_name},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

        first_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_FIRST_NAME_KEY_NAME: first_name},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

    def test_update_user_with_invalid_last_name(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
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
        access_jwt = res[RES_ACCESS_TOKEN_KEY_NAME]

        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH + 1)
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_LAST_NAME_KEY_NAME: last_name},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

        last_name = generate_lowercase_string_of_length(USER_NAME_MIN_LENGTH - 1)
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_LAST_NAME_KEY_NAME: last_name},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

    def test_update_user_with_invalid_phone(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
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
        access_jwt = res[RES_ACCESS_TOKEN_KEY_NAME]

        phone = "01234567890"
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_PHONE_KEY_NAME: phone},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

    def test_update_user_with_invalid_password_length(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
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
        access_jwt = res[RES_ACCESS_TOKEN_KEY_NAME]

        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH + 1)
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_PASSWORD_KEY_NAME: password},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

        password = generate_lowercase_string_of_length(USER_PASSWORD_MIN_LENGTH - 1)
        res = self.app.put(USER_ABS_ENDPOINT_NAME,
                            data={REQ_USER_PASSWORD_KEY_NAME: password},
                            headers=dict({REQ_JSON_WEB_TOKEN_HEADER_NAME: 'Bearer ' + access_jwt}))
        assert "400" in res.status

