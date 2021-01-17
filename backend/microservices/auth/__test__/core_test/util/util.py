import random
import string
from datetime import datetime
from core.usecases import add_user, get_user
from config import *


def generate_lowercase_string_of_length(len):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(len))


def generate_random_string_of_length(len):
    return ''.join(random.choice(string.ascii_letters) for _ in range(len))


def create_and_add_valid_user():
    first_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
    last_name = generate_lowercase_string_of_length(USER_NAME_MAX_LENGTH)
    email = generate_lowercase_string_of_length(USER_EMAIL_MAX_LENGTH - len("@gmail.com")) + "@gmail.com"
    phone = "+201234567890"
    password = generate_lowercase_string_of_length(USER_PASSWORD_MAX_LENGTH)
    gender = "m"
    birthday = datetime(1999, 7, 24)
    add_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        password=password,
        gender=gender,
        birthday=birthday,
    )
    return get_user(email=email)