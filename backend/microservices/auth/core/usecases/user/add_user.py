from core.entities import make_user


def build_add_user(insert_user):
    def add_user(first_name, last_name, phone, email, password, birthday, gender) -> bool:
        user = make_user(first_name, last_name, phone,
                         email, password, None, birthday, gender)
        return insert_user(user)
    return add_user
