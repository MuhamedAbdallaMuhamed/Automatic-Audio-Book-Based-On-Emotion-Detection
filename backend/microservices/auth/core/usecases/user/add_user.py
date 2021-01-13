from core.entities import make_user


def build_add_user(insert_user, add_image_to_storage):
    def add_user(first_name, last_name, phone, email, password, profile_picture_data, birthday, gender) -> bool:
        profile_picture_url = add_image_to_storage(profile_picture_data)
        user = make_user(first_name, last_name, phone,
                         email, password, profile_picture_url, birthday, gender)
        return insert_user(user)
    return add_user
