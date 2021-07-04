def build_delete_user(db_delete_user):
    def delete_user(id) -> bool:
        return db_delete_user(id)
    return delete_user
