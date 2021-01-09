from ..entities import make_user


def build_update_user(update_user):
    def update_user(user) -> bool:
        user = make_user(id=user.id,
                         first_name=user.first_name,
                         last_name=user.last_name,
                         email=user.email,
                         password=user.password,
                         phone=user.phone,
                         profile_picture_url=user.profile_picture_url)
        return update_user(user)
    return update_user
