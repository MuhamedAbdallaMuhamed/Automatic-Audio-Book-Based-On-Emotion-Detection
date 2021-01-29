from core.entities import edit_user


def build_update_user(db_update_user, add_image_to_storage):
    def update_user(id, first_name=None, last_name=None, email=None, password=None,
                    phone=None, profile_picture_data=None, birthday=None, gender=None, reset_code=None) -> bool:
        from .. import get_user
        if not id:
            return False
        # checking if user exist or not
        old_user = get_user(id=id)
        if not old_user:
            from . import UserDoesNotExist
            raise UserDoesNotExist
        
        if profile_picture_data:
            add_image_to_storage(old_user.id, profile_picture_data)
        edited_user = edit_user(
                        id=old_user.id,
                        first_name=first_name if first_name is not None and first_name != old_user.first_name else old_user.first_name,
                        last_name=last_name if last_name is not None and last_name != old_user.last_name else old_user.last_name,
                        email=email if email is not None and email != old_user.email else old_user.email,
                        password=password if password is not None else old_user.hashed_password,
                        salt=old_user.salt,
                        phone=phone if phone is not None and phone != old_user.phone else old_user.phone,
                        birthday=birthday if birthday is not None else old_user.birthday,
                        gender=gender if gender is not None and gender != old_user.gender else old_user.gender,
                        reset_code=reset_code,
                        new_email=email is not None and email != old_user.email,
                        new_phone=phone is not None and phone != old_user.phone,
                        new_gender=gender is not None and gender != old_user.gender,
                        new_birthday=birthday is not None,
                        new_password=password is not None,
                        new_last_name=last_name is not None and last_name != old_user.last_name,
                        new_first_name=first_name is not None and first_name != old_user.first_name,
                    )
        return db_update_user(edited_user)
    return update_user
