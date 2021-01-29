import random
import string


def send_email(mail, app, msg):
    with app.app_context():
        mail.send(msg)


def generate_random_string_of_length(len):
    return ''.join(random.choice(string.ascii_letters) for _ in range(len))
