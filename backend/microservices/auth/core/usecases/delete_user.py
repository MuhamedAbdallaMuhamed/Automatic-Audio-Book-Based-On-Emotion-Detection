def build_delete_user(delete_user):
    def delete_user(id) -> bool:
        return delete_user(id)
    return delete_user
