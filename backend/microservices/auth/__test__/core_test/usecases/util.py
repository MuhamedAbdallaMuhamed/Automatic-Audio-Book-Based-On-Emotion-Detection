import random
import string


def generate_lowercase_string_of_length(len):
    return ''.join(random.choice(string.lowercase) for _ in range(len))


def generate_random_string_of_length(len):
    return ''.join(random.choice(string.ascii_letters) for _ in range(len))
