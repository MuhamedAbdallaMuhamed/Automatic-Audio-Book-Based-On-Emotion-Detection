from core.entities import make_user


def build_add_user(insert_user):
    def add_user(id, first_name, last_name, phone, email, password, profile_picture_url) -> bool:
        user = make_user(id, first_name, last_name, phone,
                         email, password, profile_picture_url)
        return insert_user(user)
    return add_user
