import unittest
import json

from controller import app
from __test__.core_test.util import *


class AuthenticationTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_authentication_services(self):
        first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
        email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
        phone = "+201234567890"
        password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
        gender = "m"
        birthday = datetime(1999, 7, 24)

        res = self.app.post(AUTHENTICATION_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_GOOGLE_TOKEN_KEY_NAME: "eyJhbGciOiJSUzI1NiIsImtpZCI6IjAzYjJkMjJjMmZlY2Y4NzNlZDE5ZTViOGNmNzA0YWZiN2UyZWQ0YmUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI0MDc0MDg3MTgxOTIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI0MDc0MDg3MTgxOTIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTAzMzU1Mzc0NTkxMjMwNTc4ODciLCJlbWFpbCI6Im1lZG9raW5nZG9tN0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6Ii1VVUNIdHl4ZkFZSEN3TGYtM2xxaWciLCJuYW1lIjoiTWVkbyBLaW5nIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BT2gxNEdoeHFsdzYzMjRqVWV3R3dpR1JaOWdKZXczYjBCUWxCNUNpYkxncnJRPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6Ik1lZG8iLCJmYW1pbHlfbmFtZSI6IktpbmciLCJsb2NhbGUiOiJhciIsImlhdCI6MTYxMjIxODIxMCwiZXhwIjoxNjEyMjIxODEwfQ.WH0fUyAiCyQrOkOu0nSPBj4JaWXSVXTyKHEWB7GdhVhCxuuNuBEoxLqS_sZJ-fJVgK3tHZrKnLbu8R6d7s4zt8NbmdJJM_Q1gppTY3exog-wAnyxcZVfdpVgTlPun6E_uOFqQYJ9nwaMGko8BHEe4XOr-cYcaEmY7KkKTflIhchY--LEQDJb2M43g1d2q_Mgp36dIL08BISrARVXCH0IWVFddsJ0j9RR7mO4Da1autITLG5rfnLweyOlmKJdEVCWB-kk8Es4YfyZogB-MmoDfqgK6AEr-heRjjsF_bGc6h_FGRwqGQPGoc463kmxgk_72PrfsobHVProDmPFOBvGNg"})
        assert res is not None
        assert "400" in res.status
        res = json.loads(res.data)
        assert RES_MESSAGE_KEY_NAME in res
        print("test 1 passed!!")

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
        print("test 2 passed!!")

        res = self.app.post(AUTHENTICATION_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: email,
                                  REQ_GOOGLE_TOKEN_KEY_NAME: "eyJhbGciOiJSUzI1NiIsImtpZCI6IjAzYjJkMjJjMmZlY2Y4NzNlZDE5ZTViOGNmNzA0YWZiN2UyZWQ0YmUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI0MDc0MDg3MTgxOTIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI0MDc0MDg3MTgxOTIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTAzMzU1Mzc0NTkxMjMwNTc4ODciLCJlbWFpbCI6Im1lZG9raW5nZG9tN0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6Ii1VVUNIdHl4ZkFZSEN3TGYtM2xxaWciLCJuYW1lIjoiTWVkbyBLaW5nIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BT2gxNEdoeHFsdzYzMjRqVWV3R3dpR1JaOWdKZXczYjBCUWxCNUNpYkxncnJRPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6Ik1lZG8iLCJmYW1pbHlfbmFtZSI6IktpbmciLCJsb2NhbGUiOiJhciIsImlhdCI6MTYxMjIxODIxMCwiZXhwIjoxNjEyMjIxODEwfQ.WH0fUyAiCyQrOkOu0nSPBj4JaWXSVXTyKHEWB7GdhVhCxuuNuBEoxLqS_sZJ-fJVgK3tHZrKnLbu8R6d7s4zt8NbmdJJM_Q1gppTY3exog-wAnyxcZVfdpVgTlPun6E_uOFqQYJ9nwaMGko8BHEe4XOr-cYcaEmY7KkKTflIhchY--LEQDJb2M43g1d2q_Mgp36dIL08BISrARVXCH0IWVFddsJ0j9RR7mO4Da1autITLG5rfnLweyOlmKJdEVCWB-kk8Es4YfyZogB-MmoDfqgK6AEr-heRjjsF_bGc6h_FGRwqGQPGoc463kmxgk_72PrfsobHVProDmPFOBvGNg"})
        assert res is not None
        assert "200" in res.status
        res = json.loads(res.data)
        assert RES_ACCESS_TOKEN_KEY_NAME in res
        assert RES_REFRESH_TOKEN_KEY_NAME in res
        print("test 3 passed!!")

        res = self.app.post(AUTHENTICATION_ABS_ENDPOINT_NAME,
                            data={REQ_USER_EMAIL_KEY_NAME: "medokingdom7@gmail.com",
                                  REQ_GOOGLE_TOKEN_KEY_NAME: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"})
        assert res is not None
        assert "401" in res.status
        res = json.loads(res.data)
        assert RES_MESSAGE_KEY_NAME in res
        print("test 4 passed!!")
