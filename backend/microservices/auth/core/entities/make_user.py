from .user import User


def build_make_user(email_validator, password_validator):
    def make_user(id, first_name, last_name, phone, email, password, profile_picture_url):
        # vaildate id
        # vaildate email
        if not email_validator(email):
            # TODO: throw exception
            pass

        # vaildate password
        if not password_validator(email):
            # TODO: throw exception
            pass

        user = User(id, first_name, last_name, phone,
                    email, password, profile_picture_url)
        return user
    return make_user
