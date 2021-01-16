def build_is_token_exist(is_token_exist):
    def is_token_in_blocked_list(token: str) -> bool:
        return is_token_exist(token=token)
    return is_token_in_blocked_list
